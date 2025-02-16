import os
import pytest
import bz2
from src.bzip2_compression import bzip2_compress

@pytest.fixture
def sample_text_file(tmp_path):
    """Create a temporary sample text file for testing."""
    sample_file = tmp_path / "sample.txt"
    sample_file.write_text("Hello, this is a test file for Bzip2 compression!")
    return str(sample_file)

def test_bzip2_compress_default_output(sample_text_file):
    """Test compression with default output path."""
    compressed_path = bzip2_compress(sample_text_file)
    
    # Check compressed file exists
    assert os.path.exists(compressed_path)
    assert compressed_path == sample_text_file + '.bz2'
    
    # Verify compression
    with open(compressed_path, 'rb') as compressed_file:
        decompressed_data = bz2.decompress(compressed_file.read())
    
    with open(sample_text_file, 'rb') as original_file:
        assert decompressed_data == original_file.read()

def test_bzip2_compress_custom_output(sample_text_file, tmp_path):
    """Test compression with custom output path."""
    custom_output = str(tmp_path / "custom_compressed.bz2")
    compressed_path = bzip2_compress(sample_text_file, custom_output)
    
    # Check compressed file exists at custom path
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify compression
    with open(compressed_path, 'rb') as compressed_file:
        decompressed_data = bz2.decompress(compressed_file.read())
    
    with open(sample_text_file, 'rb') as original_file:
        assert decompressed_data == original_file.read()

def test_bzip2_compress_nonexistent_file():
    """Test compression of non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        bzip2_compress("/path/to/nonexistent/file.txt")

def test_bzip2_compress_invalid_input():
    """Test compression with invalid input raises ValueError."""
    with pytest.raises(ValueError):
        bzip2_compress(None)
    with pytest.raises(ValueError):
        bzip2_compress("")