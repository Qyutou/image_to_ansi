from cv2 import cv2


def load_image(image_path):
    """Return loaded image"""
    try:
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        return image
    except FileNotFoundError:
        print("File not found")


def scale_image(image, new_size=(100, 40)):
    """Scale the image to certain size"""
    required_size = [new_size[0], new_size[1]]

    # Calculate resized image size
    required_size = calculate_resized_size((image.shape[1], image.shape[0]), required_size)

    # resize image
    new_image = cv2.resize(image, (required_size[0] * 2, required_size[1]), interpolation=cv2.INTER_AREA)

    return new_image


def calculate_resized_size(current_size, required_size):
    result_size = required_size

    # If the image is square
    if current_size[0] == current_size[1]:
        if required_size[0] <= required_size[1]:
            result_size[1] = int(required_size[0])
        else:
            result_size[0] = int(required_size[1])

    # If height is smaller than width
    if current_size[1] < current_size[0]:
        # If height is smaller than width
        if required_size[1] < required_size[0]:
            result_size[1] = int(required_size[1])
            result_size[0] = int((current_size[0] / (current_size[1] / result_size[1])))

        else:
            result_size[0] = int(required_size[0])
            result_size[1] = int((current_size[1] / (current_size[0] / result_size[0])))

    # If width is smaller than height
    if current_size[0] < current_size[1]:
        # If height is smaller than width
        if required_size[1] < required_size[0]:
            result_size[0] = int(required_size[0])
            result_size[1] = int((current_size[1] / (current_size[0] / result_size[0])))
        else:
            result_size[1] = int(required_size[1])
            result_size[0] = int((current_size[0] / (current_size[1] / result_size[1])))

    return result_size

