import os
import gzip
import pytest
from src.gzip_compression import compress_file

@pytest.fixture
def sample_text_file(tmp_path):
    """Create a sample text file for testing."""
    sample_file = tmp_path / "sample.txt"
    sample_file.write_text("This is a test file for gzip compression.")
    return str(sample_file)

def test_compress_file_default_output(sample_text_file, tmp_path):
    """Test compressing a file with default output path."""
    compressed_file = compress_file(sample_text_file)
    
    # Check compressed file exists
    assert os.path.exists(compressed_file)
    assert compressed_file == sample_text_file + '.gz'
    
    # Verify file contents can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for gzip compression."

def test_compress_file_custom_output(sample_text_file, tmp_path):
    """Test compressing a file with a custom output path."""
    custom_output = str(tmp_path / "custom_compressed.gz")
    compressed_file = compress_file(sample_text_file, custom_output)
    
    # Check compressed file exists
    assert os.path.exists(compressed_file)
    assert compressed_file == custom_output
    
    # Verify file contents can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for gzip compression."

def test_compress_nonexistent_file():
    """Test compressing a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")

def test_compress_directory(tmp_path):
    """Test compressing a directory raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        compress_file(str(tmp_path))

def test_compressed_file_size(sample_text_file):
    """Test that compressed file is smaller than original file."""
    compressed_file = compress_file(sample_text_file)
    original_size = os.path.getsize(sample_text_file)
    compressed_size = os.path.getsize(compressed_file)
    
    assert compressed_size < original_size