import os
import gzip
import pytest
from src.gzip_compression import gzip_compress

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = "This is a test file for Gzip compression."
    test_file = tmp_path / "sample.txt"
    test_file.write_text(sample_content)
    return str(test_file)

def test_gzip_compress_default_output(sample_file, tmp_path):
    """Test compression with default output path"""
    compressed_file = gzip_compress(sample_file)
    
    # Verify compressed file exists
    assert os.path.exists(compressed_file)
    assert compressed_file == sample_file + '.gz'
    
    # Verify file can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for Gzip compression."

def test_gzip_compress_custom_output(sample_file, tmp_path):
    """Test compression with custom output path"""
    custom_output = str(tmp_path / "custom_compressed.gz")
    compressed_file = gzip_compress(sample_file, custom_output)
    
    # Verify compressed file exists
    assert os.path.exists(compressed_file)
    assert compressed_file == custom_output
    
    # Verify file can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for Gzip compression."

def test_gzip_compress_nonexistent_file():
    """Test compression of non-existent file raises FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        gzip_compress('/path/to/nonexistent/file.txt')

def test_gzip_compress_invalid_input():
    """Test invalid input raises ValueError"""
    with pytest.raises(ValueError):
        gzip_compress('')
    with pytest.raises(ValueError):
        gzip_compress(None)

def test_gzip_compression_large_file(tmp_path):
    """Test compression of a larger file"""
    large_file = tmp_path / "large_sample.txt"
    large_content = "X" * (1024 * 1024)  # 1 MB of content
    large_file.write_text(large_content)
    
    compressed_file = gzip_compress(str(large_file))
    
    # Verify compressed file exists
    assert os.path.exists(compressed_file)
    
    # Verify file can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == large_content