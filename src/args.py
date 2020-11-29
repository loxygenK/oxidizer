from argparse import ArgumentParser
from typing import List

class Argument:

    def __init__(self):
        self.parser = ArgumentParser(
            description="A building helper for the Rust project for Arduino.",
        )
        self.__setup_parser()
        self.__setup_fields(self.parser.parse_args())


    def __setup_parser(self):
        self.parser.add_argument(
            'target', help='Specify the serial port to write.'
        )
        self.parser.add_argument(
            '--cargo-option', '-c', metavar="Option",
            help="Pass options to cargo. Type without '-'!", nargs="*",
            dest="cargo_option"
        )
        self.parser.add_argument(
            '--avrdude-option', '-a', metavar="Option",
            help="Pass options to avrdude. Type without '-'!", nargs="*",
            dest="avrdude_option"
        )
        self.parser.add_argument(
            '--avrdude-override', '-A',
            help="override avrdude's option. Use with '-a'", action="store_true",
            dest="avrdude_override"
        )
        self.parser.add_argument(
            '--avrdude-quite', '-q',
            help="Use -q option when avrdude.", action="store_true",
            dest="avrdude_quite"
        )
        self.parser.add_argument(
            '--skip-cargo', '-s',
            help="Skip building using cargo.",
            dest="skip_cargo"
        )

    def __setup_fields(self, arguments):
        if arguments.avrdude_override and arguments.avrdude_option is None:
            raise ArgumentError(
                "--avrdude-override",
                "--avrdude-override is selected, but no options were given!"
            )
        self.target: str = arguments.target
        self.cargo_option: List[str] = list(
            map(lambda x: (("-" if len(x) == 1 else "--") + x), arguments.cargo_option)
        ) if arguments.cargo_option is not None else []
        self.avrdude_option: List[str] = list(
            map(lambda x: (("-" if len(x) == 1 else "--") + x), arguments.avrdude_option)
        ) if arguments.avrdude_option is not None else []
        self.avrdude_override: bool = arguments.avrdude_override
        self.avrdude_quite: bool = arguments.avrdude_quite
        self.skip_cargo: bool = arguments.skip_cargo


class ArgumentError(Exception):
    def __init__(self,
            argname: str, reason: str):
        super().__init__(f"'{argname}' is invalid: {reason}")
        self.argname = argname
        self.reason = reason

