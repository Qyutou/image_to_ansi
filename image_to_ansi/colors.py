import json
import math
import numpy as np


class Colors(object):
    """
    This class should handle any work with colors,
    e.g. get the closest possible color or get the prefix to use color in terminal
    """
    colors = None
    bgr_colors = np.zeros(2)

    def __init__(self, path):
        """
        Load the colors and convert it to bgr
        """
        self.load_colors(path)
        self.bgr_colors = np.zeros(shape=(len(self.colors), 3))
        self.convert_color_to_bgr()

    def load_colors(self, path):
        """
        Load list of all colors
        This list should contain rgb value of all possible colors
        """
        with open(path) as json_file:
            self.colors = json.load(json_file)

    def convert_color_to_bgr(self):
        """Convert all colors in list to bgr format"""
        bgr_list = np.empty(shape=(len(self.colors), 3))
        for i in range(len(self.colors)):
            dictionary = self.colors[i]["rgb"]
            bgr_color = (dictionary.get("b"), dictionary.get("g"), dictionary.get("r"))
            bgr_list[i, 0], bgr_list[i, 1], bgr_list[i, 2] = bgr_color
        self.bgr_colors = bgr_list

    def get_color(self, id):
        """Get specified color"""
        if self.colors is not None:
            dictionary = self.colors[id]["rgb"]
            bgr = (dictionary.get("b"), dictionary.get("g"), dictionary.get("r"))
            return bgr
        else:
            return None

    def get_closest_color(self, color):
        """
        Get the closest color to specified color from the list
        """
        if self.colors is not None:
            # Get all possible colors
            colors = self.bgr_colors

            # Get the first difference to compare in future
            prev_difference = Colors.get_difference_between_colors(color, (0, 0, 0))
            current_closest = 0

            # Main loop
            # This calculate new difference,
            # and compare it to the previously closest difference.
            for i in range(len(colors)):
                difference = Colors.get_difference_between_colors(color, colors[i])
                if difference < prev_difference:
                    prev_difference = difference
                    current_closest = i

            # Return the color as id of the color in the list of all colors
            return current_closest
        else:
            return None

    @staticmethod
    def get_difference_between_colors(color_1, color_2):
        """
        Get the difference between two colors.
        """
        difference = math.sqrt(math.pow(color_2[0] - color_1[0], 2) +
                               math.pow(color_2[1] - color_1[1], 2) +
                               math.pow(color_2[2] - color_1[2], 2))
        return difference

    @staticmethod
    def generate_color(color, foreground=True, background=True):
        text = ""

        if foreground:
            text += "\u001b[38;5;%dm" % color
        if background:
            text += "\u001b[48;5;%dm" % color

        return text

    @staticmethod
    def generate_colored_text(text, color, foreground=True, background=True):
        """Create the text with certain color"""
        return "{}{}{}".format(Colors.generate_color(color, foreground=foreground, background=background),
                               text, "\u001b[{}m".format(0))

    @staticmethod
    def generate_draw(color, background=True):
        """Create the block with certain color"""
        return Colors.generate_colored_text("█", color, background=background)
