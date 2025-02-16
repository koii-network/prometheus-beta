import os
import bz2
import pytest
from src.bzip2_decompress import decompress_bzip2_file

@pytest.fixture
def sample_compressed_file(tmp_path):
    """Create a sample bzip2 compressed file for testing"""
    content = b"This is a test file for bzip2 decompression."
    compressed_file = tmp_path / "test_compressed.bz2"
    with bz2.open(compressed_file, 'wb') as f:
        f.write(content)
    return compressed_file

def test_decompress_bzip2_file_default_output(sample_compressed_file, tmp_path):
    """Test decompression with default output filename"""
    decompressed_path = decompress_bzip2_file(str(sample_compressed_file))
    
    assert os.path.exists(decompressed_path)
    with open(decompressed_path, 'rb') as f:
        content = f.read()
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_bzip2_file_custom_output(sample_compressed_file, tmp_path):
    """Test decompression with custom output filename"""
    custom_output = str(tmp_path / "custom_output.txt")
    decompressed_path = decompress_bzip2_file(str(sample_compressed_file), custom_output)
    
    assert decompressed_path == custom_output
    assert os.path.exists(decompressed_path)
    with open(decompressed_path, 'rb') as f:
        content = f.read()
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_nonexistent_file():
    """Test handling of non-existent input file"""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("nonexistent_file.bz2")

def test_decompress_invalid_bzip2_file(tmp_path):
    """Test handling of invalid bzip2 file"""
    invalid_file = tmp_path / "invalid.bz2"
    with open(invalid_file, 'wb') as f:
        f.write(b"Not a valid bzip2 file")
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(str(invalid_file))