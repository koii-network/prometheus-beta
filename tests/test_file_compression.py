import os
import gzip
import pytest
from src.file_compression import compress_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = "This is a test file for gzip compression."
    test_file = tmp_path / "sample.txt"
    test_file.write_text(sample_content)
    return test_file

def test_compress_file_default_output(sample_file):
    """Test default compression (auto .gz extension)"""
    compressed_path = compress_file(str(sample_file))
    
    # Check compressed file was created
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.gz')
    
    # Verify contents can be decompressed correctly
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
        assert content == sample_file.read_text()

def test_compress_file_custom_output(sample_file, tmp_path):
    """Test compression with custom output path"""
    custom_output = str(tmp_path / "custom_compressed.txt.gz")
    compressed_path = compress_file(str(sample_file), custom_output)
    
    # Check compressed file was created at specified location
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify contents can be decompressed correctly
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
        assert content == sample_file.read_text()

def test_compress_nonexistent_file():
    """Test compressing a file that doesn't exist"""
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")

def test_large_file(tmp_path):
    """Test compressing a larger file"""
    large_file = tmp_path / "large_file.txt"
    large_file.write_text("A" * 1_000_000)  # 1 million characters
    
    compressed_path = compress_file(str(large_file))
    
    # Verify compression worked
    assert os.path.exists(compressed_path)
    
    # Verify contents can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        content = f.read()
        assert content == large_file.read_text()