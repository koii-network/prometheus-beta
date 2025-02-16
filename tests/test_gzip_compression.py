import os
import gzip
import pytest
from src.gzip_compression import compress_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_file_path = tmp_path / "sample.txt"
    with open(sample_file_path, 'w') as f:
        f.write("This is a test file for Gzip compression.")
    return sample_file_path

def test_compress_file_default_output(sample_file):
    """Test compression with default output path"""
    compressed_path = compress_file(str(sample_file))
    
    # Check compressed file exists
    assert os.path.exists(compressed_path)
    assert compressed_path == str(sample_file) + '.gz'
    
    # Verify compression
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for Gzip compression."

def test_compress_file_custom_output(sample_file, tmp_path):
    """Test compression with custom output path"""
    custom_output = str(tmp_path / "custom_compressed.gz")
    compressed_path = compress_file(str(sample_file), custom_output)
    
    # Check compressed file exists and is correct
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify compression
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for Gzip compression."

def test_compress_nonexistent_file():
    """Test compression of non-existent file"""
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")