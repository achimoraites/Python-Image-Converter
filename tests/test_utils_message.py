from datetime import datetime
from unittest.mock import patch
from raw_image_converter.utils import message


class TestMessage:
    # Case: converted
    def test_print_converted_file_message(self):
        file = "example.jpg"
        converted = True
        expected_message = (
            f"{datetime.now().time().strftime('%H:%M:%S')} Converted: {file}"
        )

        with patch("builtins.print") as mock_print:
            message(file, converted)

        mock_print.assert_called_once_with(expected_message)

    # Case: NOT converted
    def test_print_failed_conversion_message(self):
        file = "example.jpg"
        converted = False
        expected_message = f"{datetime.now().time().strftime('%H:%M:%S')} Conversion failed for File: {file}"

        with patch("builtins.print") as mock_print:
            message(file, converted)

        mock_print.assert_called_once_with(expected_message)
