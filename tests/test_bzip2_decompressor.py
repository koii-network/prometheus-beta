import os
import bz2
import pytest
from src.bzip2_decompressor import decompress_bzip2_file

@pytest.fixture
def create_test_bzip2_file(tmp_path):
    """Create a bzip2 compressed test file for testing."""
    test_content = b"Hello, this is a test file for bzip2 decompression."
    compressed_filepath = tmp_path / "test_compressed.bz2"
    
    with bz2.open(compressed_filepath, 'wb') as f:
        f.write(test_content)
    
    return compressed_filepath

def test_decompress_bzip2_file_default_output(create_test_bzip2_file, tmp_path):
    """Test decompressing a file with default output path."""
    compressed_filepath = create_test_bzip2_file
    decompressed_path = decompress_bzip2_file(str(compressed_filepath))
    
    assert os.path.exists(decompressed_path)
    with open(decompressed_path, 'rb') as f:
        content = f.read()
    assert content == b"Hello, this is a test file for bzip2 decompression."

def test_decompress_bzip2_file_custom_output(create_test_bzip2_file, tmp_path):
    """Test decompressing a file with a custom output path."""
    compressed_filepath = create_test_bzip2_file
    custom_output = tmp_path / "custom_output.txt"
    decompressed_path = decompress_bzip2_file(str(compressed_filepath), str(custom_output))
    
    assert decompressed_path == str(custom_output)
    with open(decompressed_path, 'rb') as f:
        content = f.read()
    assert content == b"Hello, this is a test file for bzip2 decompression."

def test_decompress_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("non_existent_file.bz2")

def test_decompress_directory():
    """Test handling of directory input."""
    with pytest.raises(IsADirectoryError):
        decompress_bzip2_file(".")  # Current directory