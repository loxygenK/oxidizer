#!/bin/python3
import toml
import os
import subprocess as sp
from args import Argument, ArgumentError

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


def main():
    package_name = fetch_package_name()
    if package_name is None:
        return

    print(f"[i] Building '{package_name}'...")
    return_code = run_command(["cargo", "build"])

    if return_code != 0:
        print("[!] Building failed! Exiting.")
        return

    print("[i] Building succeeded! Writing to Arduino...")
    arguments = [
        "avrdude",
        "-C/etc/avrdude.conf",
        "-patmega328p",
        "-carduino",
        "-P/dev/ttyUSB0",
        f"-Uflash:w:target/avr-atmega328p/debug/{package_name}.elf:e"
    ]
    return_code = run_command(arguments)

    if return_code != 0:
        print("[!] Writing failed!")

    print("[✓] All works done!")
    

if __name__ == "__main__":
    try:
        argument = Argument()
    except ArgumentError as e:
        message = e.reason
        print(f"[!] {message}")
    # main()

