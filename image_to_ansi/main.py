from colors import Colors
import image_handler as ih
import click
import sys
import re


def convert_image_to_text(image, text_size, background=True, character=None, alpha=True):
    """This method simply use the algorithm which translate image to text."""
    # Load the colors
    colors = Colors("resources/colors.json")

    # Scale image
    scaled_image = ih.scale_image(image, new_size=text_size)

    # Get the text version of image
    output_text = get_text_by_image(scaled_image, colors, background=background, character=character, alpha=alpha)

    return output_text


def get_text_by_image(image, colors, background=True, character=None, alpha=True):
    """Get text from image."""
    output_text = ""
    for x in range(image.shape[0]):
        new_line = ""
        for y in range(image.shape[1]):
            # Get the color of current pixel
            image_color = image[x, y]
            required = True

            # If this pixel is transparent then place space here
            if image.shape[2] >= 4 and alpha:
                if image_color[3] == 0:
                    new_line += " "
                    required = False
            if required:
                # Find the closest color from the possible ansi-colors
                color = colors.get_closest_color(image_color)
                # Add new character
                if character is None:
                    new_line += colors.generate_draw(color, background=background)
                else:
                    new_line += colors.generate_colored_text(character, color, background=background)
        print(new_line)
        output_text += new_line
        output_text += "\n"
    return output_text


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
                print("Successfully saved to \"%s\"" % file_name)
                file.write(text)
        else:
            with open(file_name, "a") as file:
                file.write(text)
    except FileNotFoundError:
        print("File not found: \"{}\"".format(file_name))


@click.group()
@click.version_option("1.0.0")
def main():
    """A simple application which can convert image to .ans file"""
    pass


def get_size(size):
    """
    Get the size from WWWxHHH format
    It also check if the format is correct
    """
    if re.match(r"^\d+x\d+$", size) is not None:
        sizes = [int(value) for value in re.findall(r"\d+", size)]
        return sizes
    else:
        print("Size should be in WWWxHHH format")
        return 80, 40


@main.command()
@click.option("--s", "--size", "size",
              default="80x40", show_default=True, type=str,
              help="Size of the text.")
@click.option("--bg", "--background", "background",
              default=True, show_default=True, type=bool,
              help="Should the characters use colored bg or not.")
@click.option("--c", "--character", "character",
              default=None, show_default=False, type=str,
              help="Character which used to draw image. (Default: pseudographics)")
@click.option("--a", "--alpha", "alpha",
              default=True, show_default=True, type=bool,
              help="If true the transparent parts will be transparent.")
@click.argument("input_path", type=str)
@click.argument("output_path", type=str)
def convert(size, background, character, alpha, input_path, output_path):
    """Convert image to text, and save it to file."""

    if input_path.endswith(".png") or input_path.endswith(".jpg"):
        if not output_path.endswith(".ans"):
            output_path += ".ans"
        # Get converted image
        text = convert_image_to_text(ih.load_image(input_path),
                                     text_size=get_size(size), background=background, character=character, alpha=alpha)
        # Save text
        save_to_file(text, output_path)
    else:
        print("Incorrect input file: File should be .png or .jpg")
    pass


@main.command()
@click.option("--s", "--size", "size",
              default="80x40", show_default=True, type=str,
              help="Size of the text.")
@click.option("--bg", "--background", "background",
              default=True, show_default=True, type=bool,
              help="Should the characters use colored bg or not.")
@click.option("--c", "--character", "character",
              default=None, show_default=False, type=str,
              help="Character which used to draw image. (Default: pseudographics)")
@click.option("--a", "--alpha", "alpha",
              default=True, show_default=True, type=bool,
              help="If true the transparent parts will be transparent.")
@click.argument("path", type=str)
def draw(size, background, character, alpha, path):
    """Draw image(.png or .jpg) or ansi file(.ans)."""
    # Check if file extension is image or ansi file
    if path.endswith(".ans"):
        # Print the .ans file
        print_ans_file(path)
    elif path.endswith(".png") or path.endswith(".jpg"):
        # Print the converted version
        convert_image_to_text(ih.load_image(path),
                              text_size=get_size(size), background=background, character=character, alpha=alpha)
    else:
        print("Incorrect file: File extension should be .ans, .png or .jpg")
    pass


if __name__ == "__main__":
    args = sys.argv
    main()
    pass
