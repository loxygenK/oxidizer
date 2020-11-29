#!/bin/python3
import toml
import os
import subprocess as sp
from src.args import Argument, ArgumentError

from typing import Optional, List

def fetch_package_name() -> Optional[str]:
    if not os.path.isfile("Cargo.toml"):
        print("[!] Cargo.toml not found!")
        print("    Please run this script at the root of the project.")
        return None

    with open("Cargo.toml") as f:
        cargo_setting = toml.load(f)

    if "package" not in cargo_setting:
        print("[!] '[Package]' not found in 'Cargo.toml'!")
        print("    Is your Cargo.toml valid?")
        return None

    if "name" not in cargo_setting["package"]:
        print("[!] 'name' not found in 'Cargo.toml'->[package]!")
        print("    Is your Cargo.toml valid?")
        return None

    if type(cargo_setting["package"]["name"]) is not str:
        print("[!] The package's name is not str!")
        print("    Is your Cargo.toml valid?")
        return None

    return cargo_setting["package"]["name"]


def run_command(args: List[str]):
    command_string = " ".join(args)
    print(f">> {command_string}")
    return sp.call(args)


def run_cargo(package_name: str, cargo_option: List[str], release: bool):
    release_text = "in release mode" if release else ""
    argument = ["cargo", "build"] + (["--release"] if release else []) + cargo_option
    print(f"[i] Building '{package_name}' {release_text}...")
    return run_command(argument)


def run_avrdude(
    target: str,
    elf_path: str,
    avrdude_option: List[str],
    avrdude_override: bool
    ):
    # TODO: Does this work in Windows? (Test required)
    if not os.path.exists(target):
        print(f"[!] {target} does not exist!")
        print("    Make sure you specified the correct device path.")
        return
    arguments = [
        "avrdude",
        "-C/etc/avrdude.conf",
        "-patmega328p",
        "-carduino",
        f"-P{target}",
        f"-Uflash:w:{elf_path}:e",
        *avrdude_option
    ] if not avrdude_override else ["avrdude", *avrdude_option]
    return run_command(arguments)


def main(argument: Argument):
    elf_path = argument.elf_path
    if not argument.skip_cargo:
        package_name = fetch_package_name()
        cargo_result = run_cargo(
            package_name,
            argument.cargo_option,
            argument.release,
        )
        if cargo_result != 0:
            print("[!] Building failed! Exiting.")
            return
        
        if elf_path is None:
            target_directory = "release" if argument.release else "debug"
            elf_path = "target/avr-atmega328p/" + \
                      f"{target_directory}/{package_name}.elf"
        print("[i] Building succeeded! Writing to Arduino...")

    avrdude_result = run_avrdude(
        argument.target,
        elf_path,
        argument.avrdude_option,
        argument.avrdude_override
    )
    if avrdude_result != 0:
        print("[!] Writing failed!")

    print("[✓] All works done!")


def entry():
    try:
        argument = Argument()
    except ArgumentError as e:
        message = e.reason
        print(f"[!] {message}")
    else:
        main(argument)


if __name__ == "__main__":
    entry()

