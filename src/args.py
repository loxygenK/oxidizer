from argparse import ArgumentParser

class Argument:

    def __init__(self):
        self.parser = ArgumentParser(
            description="A building helper for the Rust project for Arduino.",
        )
        self.__setup_parser()
        self.args = self.parser.parse_args()


    def __setup_parser(self):
        self.parser.add_argument(
            'subcommand', help='Specify what to do.',
            choices=["build", "help"]
        )
        self.parser.add_argument(
            '--cargo-option', '-c', metavar="Option",
            help="Pass options to cargo.", nargs="*"
        )
        self.parser.add_argument(
            '--cargo-override', '-C',
            help="override avrdude's option. Use with '-a'", action="store_true"
        )
        self.parser.add_argument(
            '--avrdude-option', '-a', metavar="Option",
            help="Pass options to avrdude.", nargs="*"
        )
        self.parser.add_argument(
            '--avrdude-quite', '-q',
            help="Use -q option when avrdude.", action="store_true"
        )
        self.parser.add_argument(
            '--avrdude-override', '-A',
            help="override avrdude's option. Use with '-a'", action="store_true"
        )

