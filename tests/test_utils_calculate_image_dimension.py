from raw_image_converter.utils import calculate_image_dimension


class TestCalculateImageDimension:
    # Case: resolution is a set number
    def test_valid_integer_dimension_and_resolution(self):
        dimension = 100
        resolution = "200"
        expected_result = 200

        result = calculate_image_dimension(dimension, resolution)

        assert result == expected_result

    # Case: resolution is a percentage
    def test_valid_integer_dimension_and_percentage_resolution(self):
        dimension = 100
        resolution = "50%"
        expected_result = 50

        result = calculate_image_dimension(dimension, resolution)

        assert result == expected_result
