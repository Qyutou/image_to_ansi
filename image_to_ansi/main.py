from cv2 import cv2
import numpy as np


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
            return "\u001b[{}m\u001b[{}m".format(color, color + 10)
        else:
            return "\u001b[{};1m\u001b[{};1m".format(color, color + 10)
    else:
        return "\u001b[{}m".format(color)


def generate_colored_text(text, color, bright=False):
    """Create the text with certain color"""
    return "{}{}".format(generate_color(color, bright=bright), text)


def generate_draw(color, bright=False):
    """Create the block with certain color"""
    return generate_colored_text("█{}".format(generate_color(Colors.reset)), color, bright=bright)


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


def load_image(image_path):
    """Return loaded image"""
    try:
        image = cv2.imread(image_path)
        return image
    except FileNotFoundError:
        print("File not found")


def scale_image(image, new_size=[80, 25]):
    """Scale the image to certain size"""
    # If the image is square
    if image.shape[0] == image.shape[1]:
        if new_size[0] <= new_size[1]:
            new_size[1] = new_size[0]
        else:
            new_size[0] = new_size[1]

    # Calculate coefficients
    coefficient_x = image.shape[0] / new_size[0]
    coefficient_y = image.shape[1] / new_size[1]
    new_image = np.zeros((new_size[1], new_size[0], 3), np.uint8)

    # Main loop which scale image
    for y in range(new_size[1]):
        for x in range(new_size[0]):
            average_color = get_average_section_color(image,
                                                      int(y*coefficient_y), int(x*coefficient_x),
                                                      int(coefficient_y), int(coefficient_x))
            if average_color is not None:
                new_image[y, x] = average_color

    return new_image


def get_average_section_color(image, x, y, width, height):
    """Get average color in section"""
    # Check if is it possible to get color
    if x >= image.shape[0] or y >= image.shape[1]:
        return None

    # Initialize variables
    iteration = 0
    ac_b, ac_g, ac_r = (0, 0, 0)

    # Main loop which goes over the image's section
    for dx in range(width):
        for dy in range(height):
            # Check if is it possible to get color
            if not x + dx >= image.shape[0] or y + dy >= image.shape[1]:
                # Calculate new average color
                iteration += 1
                n_b, n_g, n_r = image[x + dx, y + dy]
                ac_b = (ac_b + n_b)
                ac_g = (ac_g + n_g)
                ac_r = (ac_r + n_r)

    ac_b /= iteration
    ac_g /= iteration
    ac_r /= iteration

    # Return colors
    return int(ac_b), int(ac_g), int(ac_r)


def convert_image_to_text(image, text_size=[80, 25]):
    # Scale image
    scaled_image = scale_image(image, new_size=text_size)

    cv2.imshow("scaled image", scaled_image)
    cv2.waitKey(5000)


def print_test_image():
    convert_image_to_text(load_image("image_to_ansi/resources/image.png"))
    # print_ans_file("image_to_ansi/output/test.ans")


def main():
    """A simple application which can convert image to .ans file"""
    print_test_image()
    pass


if __name__ == "__main__":
    main()
