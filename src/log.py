from color import bold, ConsoleBaseColor

class Logger:

    def __init__(self, use_color: bool):
        self.use_color = use_color

    def print_with_tag(tag_char: str, color: ConsoleBaseColor, text: str):
        tag = (bold(color.paint(f"[{tag_char}]"))) \
              if self.use_color else "[{tag_char}]"
        indented = "    ".join(text.split())
        main_text = color.paint(indented) if self.use_color else indented
        print(tag + indented)
    
    def info(text: str):
        print_with_tag("i", ConsoleBaseColor.CYAN, text)

    def error(text: str):
        print_with_tag("!", ConsoleBaseColor.RED, text)

    def success(text: str):
        print_with_tag("✓", ConsoleBaseColor.GREEN, text)

