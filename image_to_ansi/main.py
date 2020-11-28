class Colors(object):
    """Container of all required colors."""
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    white = 37
    reset = 0


def generate_color(color, bright=False):
    """Use color code to create the correct construction to use this color"""
    if color != 0:
        if not bright:
            return "\u001b[{}m\u001b[{}m".format(color, color+10)
        else:
            return "\u001b[{};1m\u001b[{};1m".format(color, color+10)
    else:
        return "\u001b[{}m".format(color)


def generate_colored_text(text, color, bright=False):
    """Create the text with certain color"""
    return "{}{}".format(generate_color(color, bright=bright), text)


def print_ans_file(file_name):
    """Prints .ans file"""
    try:
        with open(file_name, "r") as file:
            print(*file)
    except FileNotFoundError:
        print("File not found: \"{}\"".format(file_name))


def save_to_file(text, file_name, override=True):
    """
    Save str to file_name file.
    This method is used to save ansi graphics results.
    :param text: ansi string to save
    :param file_name: file where the str should be saved.
    :param override: if True, then the str will override the file.
    """
    try:
        if override:
            with open(file_name, "w") as file:
                file.write(text)
        else:
            with open(file_name, "a") as file:
                file.write(text)
    except FileNotFoundError:
        print("File not found: \"{}\"".format(file_name))


def print_test_image():
    save_to_file(generate_colored_text("█", Colors.red), "image_to_ansi/output/test.ans", override=False)
    print_ans_file("image_to_ansi/output/test.ans")


def main():
    """A simple application which can convert image to .ans file"""
    print_test_image()
    pass


if __name__ == "__main__":
    main()
