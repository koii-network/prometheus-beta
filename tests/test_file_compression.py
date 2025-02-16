import os
import bz2
import pytest
from src.file_compression import compress_file_bzip2

@pytest.fixture
def sample_text_file(tmp_path):
    """Create a temporary text file for testing"""
    test_file = tmp_path / "sample.txt"
    test_file.write_text("This is a test file for bzip2 compression.")
    return str(test_file)

def test_compress_file_bzip2_default_output(sample_text_file, tmp_path):
    """Test compression with default output path"""
    compressed_path = compress_file_bzip2(sample_text_file)
    
    assert os.path.exists(compressed_path)
    assert compressed_path == sample_text_file + '.bz2'
    
    # Verify compression
    with bz2.open(compressed_path, 'rt') as f:
        content = f.read()
    assert content == "This is a test file for bzip2 compression."

def test_compress_file_bzip2_custom_output(sample_text_file, tmp_path):
    """Test compression with custom output path"""
    custom_output = str(tmp_path / "custom_compressed.bz2")
    compressed_path = compress_file_bzip2(sample_text_file, custom_output)
    
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify compression
    with bz2.open(compressed_path, 'rt') as f:
        content = f.read()
    assert content == "This is a test file for bzip2 compression."

def test_compress_nonexistent_file():
    """Test compression of non-existent file"""
    with pytest.raises(FileNotFoundError):
        compress_file_bzip2('/path/to/nonexistent/file.txt')

def test_compress_directory(tmp_path):
    """Test compression of a directory"""
    with pytest.raises(IsADirectoryError):
        compress_file_bzip2(str(tmp_path))