import os
import bz2
import pytest
from src.file_compression import compress_file_bzip2

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = b"This is a test file for bzip2 compression."
    file_path = tmp_path / "sample_file.txt"
    file_path.write_bytes(sample_content)
    return file_path

def test_compress_file_bzip2_default_output(sample_file):
    """Test compression with default output filename"""
    compressed_path = compress_file_bzip2(str(sample_file))
    
    # Check compressed file was created
    assert os.path.exists(compressed_path)
    assert compressed_path == str(sample_file) + '.bz2'
    
    # Verify compression
    with bz2.open(compressed_path, 'rb') as compressed_file:
        decompressed_content = compressed_file.read()
    
    assert decompressed_content == sample_file.read_bytes()

def test_compress_file_bzip2_custom_output(sample_file, tmp_path):
    """Test compression with custom output filename"""
    custom_output = str(tmp_path / "custom_compressed.bz2")
    compressed_path = compress_file_bzip2(str(sample_file), custom_output)
    
    # Check compressed file was created
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify compression
    with bz2.open(compressed_path, 'rb') as compressed_file:
        decompressed_content = compressed_file.read()
    
    assert decompressed_content == sample_file.read_bytes()

def test_compress_file_not_found():
    """Test behavior when input file does not exist"""
    with pytest.raises(FileNotFoundError):
        compress_file_bzip2("/path/to/nonexistent/file.txt")

def test_compress_empty_file(tmp_path):
    """Test compression of an empty file"""
    empty_file = tmp_path / "empty_file.txt"
    empty_file.touch()
    
    compressed_path = compress_file_bzip2(str(empty_file))
    
    # Check compressed file was created
    assert os.path.exists(compressed_path)
    
    # Verify empty file compression
    with bz2.open(compressed_path, 'rb') as compressed_file:
        decompressed_content = compressed_file.read()
    
    assert decompressed_content == b''