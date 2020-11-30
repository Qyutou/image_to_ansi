import unittest
import image_handler as ih


class ImageResizeTest(unittest.TestCase):

    def test_scaling_rectangle_with_bigger_width(self):
        # Test with required size width bigger than height
        image_size = [20, 10]
        required_size = [20, 5]
        expected_size = [10, 5]
        result_size = ih.calculate_resized_size(image_size, required_size)
        self.assertEqual(result_size, expected_size, "1. Expected [%d, %d], but got [%d, %d]" %
                         (expected_size[0], expected_size[1], result_size[0], result_size[1]))

        # Test with required size width smaller than height
        image_size = [40, 20]
        required_size = [10, 20]
        expected_size = [10, 5]
        result_size = ih.calculate_resized_size(image_size, required_size)
        self.assertEqual(result_size, expected_size, "2. Expected [%d, %d], but got [%d, %d]" %
                         (expected_size[0], expected_size[1], result_size[0], result_size[1]))

        # Test with required size width specific image
        image_size = [1600, 900]
        required_size = [80, 25]
        expected_size = [44, 25]
        result_size = ih.calculate_resized_size(image_size, required_size)
        self.assertEqual(result_size, expected_size, "3. Expected [%d, %d], but got [%d, %d]" %
                         (expected_size[0], expected_size[1], result_size[0], result_size[1]))

    def test_scaling_rectangle_with_bigger_height(self):
        # Test with required size width bigger than height
        image_size = [10, 20]
        required_size = [20, 5]
        expected_size = [5, 10]
        result_size = ih.calculate_resized_size(image_size, required_size)
        self.assertEqual(result_size, expected_size, "1. Expected [%d, %d], but got [%d, %d]" %
                         (expected_size[0], expected_size[1], result_size[0], result_size[1]))

        # Test with required size width smaller than height
        image_size = [20, 40]
        required_size = [10, 20]
        expected_size = [5, 10]
        result_size = ih.calculate_resized_size(image_size, required_size)
        self.assertEqual(result_size, expected_size, "2. Expected [%d, %d], but got [%d, %d]" %
                         (expected_size[0], expected_size[1], result_size[0], result_size[1]))

        # Test with required size width specific image
        image_size = [900, 1600]
        required_size = [80, 25]
        expected_size = [25, 44]
        result_size = ih.calculate_resized_size(image_size, required_size)
        self.assertEqual(result_size, expected_size, "3. Expected [%d, %d], but got [%d, %d]" %
                         (expected_size[0], expected_size[1], result_size[0], result_size[1]))

    def test_scaling_square(self):
        image_size = [20, 20]
        required_size = [20, 5]
        expected_size = [5, 5]
        result_size = ih.calculate_resized_size(image_size, required_size)
        self.assertEqual(result_size, expected_size, "Expected [%d, %d], but got [%d, %d]" %
                         (expected_size[0], expected_size[1], result_size[0], result_size[1]))


if __name__ == "__main__":
    unittest.main()