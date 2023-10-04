from unittest.mock import patch
from raw_image_converter.utils import check_file_type


class TestCheckFileType:
    # Case: Returns "RAW" if file extension is raw
    def test_returns_raw_if_extension_in_raw_conversion_array(self):
        extensions= [
            ".dng",
            ".raw",
            ".cr2",
            ".crw",
            ".erf",
            ".raf",
            ".kdc",
            ".dcr",
            ".mos",
            ".mef",
            ".nef",
            ".orf",
            ".rw2",
            ".pef",
            ".x3f",
            ".srw",
            ".srf",
            ".sr2",
            ".arw",
            ".mdc",
            ".mrw",
        ]

        for ext in extensions:
            assert check_file_type(f"file{ext}") == "RAW"

    # Case: Returns "NOT RAW" if file extension is not raw
    def test_returns_not_raw_if_extension_in_conversion_array(self):
        extensions2 = [".ppm", ".psd", ".webp", ".tiff"]

        for ext in extensions2:
            assert check_file_type(f"file{ext}") == "NOT RAW"

    # Case: Calls ai_2_pdf function if file extension is ".ai"
    def test_calls_ai_2_pdf_if_extension_is_ai(self):
        with patch("os.rename") as mock_rename:
            check_file_type("file.ai")
            mock_rename.assert_called_once_with("file.ai", "file.ai.pdf")

