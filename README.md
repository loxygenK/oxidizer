# oxidizer (arduino-oxidizer)

<a name="english-version" />
<a href="#japanese-version"><b>日本語版が使用できます ／ Japanese version is avaialble</b></a>

A python tool to build Rust project for Arduino and write it.

## Installation

### Requirements

- `python3`
- `pip`
- `cargo`
- A rust project configurated to build for Arduino, or an elf file to write
  - If you need to make a project for it, a template [loxygenK/arduino-on-rust_template](https://github.com/loxygenK/arduino-on-rust_template) is available.
- `avrdude`

### Installation

You can install oxidizer with`pip`

```bash
pip install arduino-oxidizer
```

Note: The package's name to install is **`arduino-oxidizer`**, not `oxidizer`. 

## How to use

### Build and write a Cargo project configured for Arduino

Oxidizer builds the project using `cargo`, and write to Arduino. The target ELF file is searched based on `cargo.toml`.

```bash
oxidizer <Serial port to write>
```

#### example

```
$ cd /path/to/cargo/projects/root
$ oxidizer /dev/ttyUSB0
[i] Building 'some-nice-project' ...
[i] >> cargo build
    Updating crates.io index
    Finished dev [unoptimized + debuginfo] target(s) in 2.30s
[v] Building succeeded! Writing to Arduino...
[i] >> avrdude -C/etc/avrdude.conf -patmega328p -carduino -P/dev/ttyUSB0 -Uflash:w:target/avr-atmega
328p/debug/some-nice-project.elf:e

avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.00s

/* ...... */

avrdude: 4982 bytes of flash verified

avrdude: safemode: Fuses OK (E:00, H:00, L:00)

avrdude done.  Thank you.

[v] All works done!
```

### Build and write in release mode

Run with the option `--release` (`-r`) , to build in release mode.

```
$ cd /path/to/cargo/projects/root
$ oxidizer /dev/ttyUSB0 -r
[i] Building 'some-nice-project' in release mode...
[i] >> cargo build --release
    Updating crates.io index
    Finished release [optimized] target(s) in 2.42s

/* ...... */

avrdude done.  Thank you.

[✓] All works done!
```

### Write your own ELF file

Run with the option `--skip-cargo` (`-s`) and `--elf-path` (`-e`) , to skip building a cargo project, and write your own ELF file to Arduino.

```
$ oxidizer --skip-cargo --elf-path my_own_elf_file.elf /dev/ttyUSB0
[i] >> avrdude -C/etc/avrdude.conf -patmega328p -carduino -P/dev/ttyUSB0 -Uflash:w:my_own_elf_file.elf:e

avrdude: AVR device initialized and ready to accept instructions

/* ...... */

avrdude done.  Thank you.

[✓] All works done!
```

## Other options

Various options is available:

```
$ oxidizer --help
usage: oxidizer [-h] [--release] [--cargo-option [Option [Option ...]]]
                [--avrdude-option [Option [Option ...]]] [--avrdude-override] [--avrdude-quite]
                [--skip-cargo] [--elf-path ELF_PATH] [--no-color]
                target

A building helper for the Rust project for Arduino.

positional arguments:
  target                Specify the serial port to write.

optional arguments:
  -h, --help            show this help message and exit
  --release, -r         Let cargo build in release mode
  --cargo-option [Option [Option ...]], -c [Option [Option ...]]
                        Pass options to cargo. Type without '-'!
  --avrdude-option [Option [Option ...]], -a [Option [Option ...]]
                        Pass options to avrdude. Type without '-'!
  --avrdude-override, -A
                        override avrdude's option. Use with '-a'
  --avrdude-quite, -q   Use -q option when avrdude.
  --skip-cargo, -s      Skip building using cargo.
  --elf-path ELF_PATH, -e ELF_PATH
                        Specify ELF file's path. Use target/avr-
                        atmega328p/{debug,release}/{package_name}.elf as default.
  --no-color            Disable color output.
```

| Option               | Abbreviation | Arguments                                               | Description                                                  |
| -------------------- | ------------ | ------------------------------------------------------- | ------------------------------------------------------------ |
| `--release`          | `-r`         | Nothing                                                 | Build the cargo project in release mode.<br />Cannot be used with `--skip-cargo`. |
| `--cargo-option`     | `-c`         | Options to pass to cargo<br />(enumerate without`-`)    | Run cargo with additional options.                           |
| `--avrdude-option`   | `-a`         | Options to pass to avrdude<br /> (enumerate without`-`) | Run avrdude with additional options.                         |
| `--avrdude-override` | `-A`         | Nothing                                                 | Replace the default options to pass to avrdude with the options specified in `--avrdude-option`. |
| `--skip-cargo`       | `-s`         | Nothing                                                 | Skip building a cargo project. Use with`--elf-path`.         |
| `--elf-path`         | `-e`         | The ELF file to write                                   | Specify the ELF file's path to write.                        |
| `--no-color`         | Nothing      | Nothing                                                 | Print logs without ASCII espace sequences.                   |

---



# oxidizer (arduino-oxidizer)

<a name="japanese-version" />
<a href="#english-version"><b>English version is available ／ 英語版が利用できます</b></a>

Pythonで作成された、Rustで書かれたArduinoプロジェクトをビルド・書き込むためのツールです。

## インストール

### 必要なもの

- `python3`
- `pip`
- `cargo`
- Arduino用にビルドできるように構成されたRustのプロジェクト
  または書き込みたいelfファイル
  - よろしければ [loxygenK/arduino-on-rust_template](https://github.com/loxygenK/arduino-on-rust_template) をどうぞ（ダイマ）
- `avrdude`

### インストール

`pip`でインストールできます:

```bash
pip install arduino-oxidizer
```

注意: インストールするパッケージ名は`oxidizer`ではなく**`arduino-oxidizer`**です。 

## 使い方

### Arduino用に構成されたCargoプロジェクトをビルド・書き込み

oxidizerは、`cargo`を用いてビルドを行い、`avrdude`を用いてArduinoへ書き込みを行います。
書き込むELFファイルは`Cargo.toml`から読み込んだプロジェクト名を元に検索されます。

```bash
oxidizer <書き込み先のシリアルポート>
```

#### 例

```
$ cd /path/to/cargo/projects/root
$ oxidizer /dev/ttyUSB0
[i] Building 'some-nice-project' ...
[i] >> cargo build
    Updating crates.io index
    Finished dev [unoptimized + debuginfo] target(s) in 2.30s
[v] Building succeeded! Writing to Arduino...
[i] >> avrdude -C/etc/avrdude.conf -patmega328p -carduino -P/dev/ttyUSB0 -Uflash:w:target/avr-atmega
328p/debug/some-nice-project.elf:e

avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.00s

/* ...... */

avrdude: 4982 bytes of flash verified

avrdude: safemode: Fuses OK (E:00, H:00, L:00)

avrdude done.  Thank you.

[v] All works done!
```

### Cargoプロジェクトをリリースモードでビルド・書き込み

`--release`（`-r`）をつけて実行すると、リリースモードでビルドされます。

```
$ cd /path/to/cargo/projects/root
$ oxidizer /dev/ttyUSB0 -r
[i] Building 'some-nice-project' in release mode...
[i] >> cargo build --release
    Updating crates.io index
    Finished release [optimized] target(s) in 2.42s

/* ...... */

avrdude done.  Thank you.

[✓] All works done!
```

### 自作のELFファイルを書き込む

`--skip-cargo`（`-s`）と`--elf-path`（`-e`）を指定して実行すると、Cargoプロジェクトのビルドをスキップし、自作のELFファイルを書き込むことができます。

```
$ oxidizer --skip-cargo --elf-path my_own_elf_file.elf /dev/ttyUSB0
[i] >> avrdude -C/etc/avrdude.conf -patmega328p -carduino -P/dev/ttyUSB0 -Uflash:w:my_own_elf_file.elf:e

avrdude: AVR device initialized and ready to accept instructions

/* ...... */

avrdude done.  Thank you.

[✓] All works done!
```

## 他のオプション

様々なオプションを利用できます:

```
$ oxidizer --help
usage: oxidizer [-h] [--release] [--cargo-option [Option [Option ...]]]
                [--avrdude-option [Option [Option ...]]] [--avrdude-override] [--avrdude-quite]
                [--skip-cargo] [--elf-path ELF_PATH] [--no-color]
                target

A building helper for the Rust project for Arduino.

positional arguments:
  target                Specify the serial port to write.

optional arguments:
  -h, --help            show this help message and exit
  --release, -r         Let cargo build in release mode
  --cargo-option [Option [Option ...]], -c [Option [Option ...]]
                        Pass options to cargo. Type without '-'!
  --avrdude-option [Option [Option ...]], -a [Option [Option ...]]
                        Pass options to avrdude. Type without '-'!
  --avrdude-override, -A
                        override avrdude's option. Use with '-a'
  --avrdude-quite, -q   Use -q option when avrdude.
  --skip-cargo, -s      Skip building using cargo.
  --elf-path ELF_PATH, -e ELF_PATH
                        Specify ELF file's path. Use target/avr-
                        atmega328p/{debug,release}/{package_name}.elf as default.
  --no-color            Disable color output.
```

| オプション           | 省略形 | 引数                                   | 説明                                                         |
| -------------------- | ------ | -------------------------------------- | ------------------------------------------------------------ |
| `--release`          | `-r`   | なし                                   | Cargoプロジェクトをリリースモードでビルドします。<br />`--skip-cargo`と同時に指定することはできません。 |
| `--cargo-option`     | `-c`   | Cargoに渡すオプション(`-`なしで列挙)   | Cargoでビルドする際に、追加でオプションをつけて実行します。  |
| `--avrdude-option`   | `-a`   | avrdudeに渡すオプション(`-`なしで列挙) | avrdudeでビルドする際に、追加でオプションをつけて実行します。 |
| `--avrdude-override` | `-A`   | なし                                   | avrdudeでビルドする際、規定のコマンドを`--avrdude-option`で指定されたものに置き換えます。 |
| `--skip-cargo`       | `-s`   | なし                                   | Cargoでのビルドをスキップします。<br />`--elf-path`と一緒に使用します。 |
| `--elf-path`         | `-e`   | Arduinoに書き込むELFファイルへのパス   | 書き込むELFファイルのパスを指定します。                      |
| `--no-color`         | なし   | なし                                   | ASCIIエスケープシーケンスなしで出力を行います。              |

