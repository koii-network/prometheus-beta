import os
import gzip
import pytest
from src.gzip_compression import compress_file

def test_compress_file(tmp_path):
    # Create a test file
    test_content = b"This is a test file for gzip compression."
    test_input = tmp_path / "test_input.txt"
    test_input.write_bytes(test_content)

    # Compress the file
    compressed_path = compress_file(str(test_input))

    # Verify compressed file exists
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.gz')

    # Verify file contents can be decompressed correctly
    with gzip.open(compressed_path, 'rb') as f:
        decompressed_content = f.read()
        assert decompressed_content == test_content

def test_compress_file_custom_output(tmp_path):
    # Create a test file
    test_content = b"Custom output path test."
    test_input = tmp_path / "test_input.txt"
    test_input.write_bytes(test_content)

    # Custom output path
    custom_output = str(tmp_path / "custom_compressed.gz")
    compressed_path = compress_file(str(test_input), custom_output)

    # Verify compressed file exists at custom path
    assert compressed_path == custom_output
    assert os.path.exists(compressed_path)

def test_compress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")

def test_compress_directory(tmp_path):
    with pytest.raises(IsADirectoryError):
        compress_file(str(tmp_path))