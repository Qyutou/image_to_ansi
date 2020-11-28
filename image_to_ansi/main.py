class Colors(object):
    """Container of all required colors."""
    black = "30"
    bright_black = "30;1"
    red = "31"
    bright_red = "31;1"
    green = "32"
    bright_green = "32;1"
    yellow = "33"
    bright_yellow = "33;1"
    blue = "34"
    bright_blue = "34;1"
    magenta = "35"
    bright_magenta = "35;1"
    cyan = "36"
    bright_cyan = "36;1"
    white = "37"
    bright_white = "37;1"
    reset = "0"


def generate_color(color):
    """Use color code to create the correct construction to use this color"""
    return "\u001b[{}m".format(color)


def generate_colored_text(text, color):
    """Create the text with certain color"""
    return "{}{}".format(generate_color(color), text)


def print_ans_file(file_name):
    """Prints .ans file"""
    try:
        with open(file_name, "r") as file:
            print(*file)
    except FileNotFoundError:
        print("File not found: \"{}\"".format(file_name))


def print_test_image():
    print_ans_file("image_to_ansi/output/test.ans")


def main():
    """A simple application which can convert image to .ans file"""
    print_test_image()
    pass


if __name__ == "__main__":
    main()
