from src.color import bold, ConsoleBaseColor

class Logger:
    __USE_COLOR = True

    @classmethod
    def print_with_tag(cls, tag_char: str, color: ConsoleBaseColor, text: str):
        tag = (bold(color.paint(f"[{tag_char}] "))) \
              if cls.__USE_COLOR else f"[{tag_char}] "
        indented = "\n    ".join(text.split("\n"))
        main_text = color.paint(indented) if cls.__USE_COLOR else indented
        print(tag + main_text)
    
    @classmethod
    def info(cls, text: str):
        cls.print_with_tag("i", ConsoleBaseColor.CYAN, text)

    @classmethod
    def error(cls, text: str):
        cls.print_with_tag("!", ConsoleBaseColor.RED, text)

    @classmethod
    def success(cls, text: str):
        cls.print_with_tag("✓", ConsoleBaseColor.GREEN, text)

    @classmethod
    def disable_color(cls):
        cls.__USE_COLOR = False

