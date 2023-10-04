from raw_image_converter.utils import split_file_extension


class TestSplitFileExtension:
    # Case: Test with a file name with an extension
    def test_extension(self):
        file = "example.jpg"
        result = split_file_extension(file)
        assert result == ("example", ".jpg")

    # Case: Test with a file name with no extension
    def test_no_extension(self):
        file = "example"
        result = split_file_extension(file)
        assert result == ("example", "")

    # Case: Test with an empty file name
    def test_empty_file_name(self):
        file = ""
        result = split_file_extension(file)
        assert result == ("", "")

    # Case: Test with a file name starting with a dot
    def test_starting_with_dot(self):
        file = ".example"
        result = split_file_extension(file)
        assert result == (".example", "")

    # Case: Test with a file name containing multiple dots
    def test_multiple_dots(self):
        file = "example.file.with.dots"
        result = split_file_extension(file)
        assert result == ("example.file.with", ".dots")
