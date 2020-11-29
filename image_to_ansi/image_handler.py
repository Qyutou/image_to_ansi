from cv2 import cv2
import numpy as np


def load_image(image_path):
    """Return loaded image"""
    try:
        image = cv2.imread(image_path)
        return image
    except FileNotFoundError:
        print("File not found")


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


def scale_image(image, new_size=(80, 25)):
    """Scale the image to certain size"""
    required_size = [new_size[0], new_size[1]]
    # If the image is square
    if image.shape[0] == image.shape[1]:
        if required_size[0] <= required_size[1]:
            required_size[1] = int(required_size[0] / 2)
        else:
            required_size[0] = int(required_size[1] * 2)

    # Calculate coefficients
    coefficient_x = image.shape[0] / required_size[0]
    coefficient_y = image.shape[1] / required_size[1]
    new_image = np.zeros((required_size[1], required_size[0], 3), np.uint8)

    # Main loop which scale image
    for y in range(required_size[1]):
        for x in range(required_size[0]):
            average_color = get_average_section_color(image,
                                                      int(y * coefficient_y), int(x * coefficient_x),
                                                      int(coefficient_y), int(coefficient_x))
            if average_color is not None:
                new_image[y, x] = average_color

    return new_image


