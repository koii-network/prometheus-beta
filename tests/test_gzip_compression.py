import os
import gzip
import pytest
import shutil

from src.gzip_compression import compress_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = "This is a test file for gzip compression."
    test_file = tmp_path / "sample.txt"
    test_file.write_text(sample_content)
    return test_file

def test_compress_file_default_output(sample_file, tmp_path):
    """Test compression with default output path"""
    compressed_path = compress_file(str(sample_file))
    
    # Check compressed file exists
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.gz')
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
    
    assert content == sample_file.read_text()

def test_compress_file_custom_output(sample_file, tmp_path):
    """Test compression with custom output path"""
    custom_output = str(tmp_path / "custom_compressed.gz")
    compressed_path = compress_file(str(sample_file), custom_output)
    
    # Check compressed file exists at the specified path
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
    
    assert content == sample_file.read_text()

def test_compress_nonexistent_file():
    """Test compressing a non-existent file raises FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")

def test_compress_directory(tmp_path):
    """Test compressing a directory raises IsADirectoryError"""
    with pytest.raises(IsADirectoryError):
        compress_file(str(tmp_path))