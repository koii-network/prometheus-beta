import os
import pytest
import zstandard as zstd
from src.zstandard_compression import compress_file, decompress_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing."""
    sample_content = "This is a test file for Zstandard compression!"
    test_file = tmp_path / "sample.txt"
    test_file.write_text(sample_content)
    return test_file

def test_compress_file(sample_file, tmp_path):
    """Test file compression functionality."""
    compressed_file = compress_file(str(sample_file))
    
    # Verify compressed file exists
    assert os.path.exists(compressed_file)
    assert compressed_file.endswith('.zst')
    
    # Verify file size is smaller than original
    original_size = os.path.getsize(sample_file)
    compressed_size = os.path.getsize(compressed_file)
    assert compressed_size < original_size

def test_decompress_file(sample_file, tmp_path):
    """Test file decompression functionality."""
    # Compress the file first
    compressed_file = compress_file(str(sample_file))
    
    # Decompress the file
    decompressed_file = decompress_file(compressed_file)
    
    # Verify decompressed file content matches original
    assert os.path.exists(decompressed_file)
    with open(decompressed_file, 'r') as f:
        content = f.read()
    
    with open(sample_file, 'r') as f:
        original_content = f.read()
    
    assert content == original_content

def test_compression_level(sample_file):
    """Test different compression levels."""
    levels_to_test = [1, 5, 10, 22]
    for level in levels_to_test:
        compressed_file = compress_file(str(sample_file), compression_level=level)
        assert os.path.exists(compressed_file)

def test_nonexistent_input_file():
    """Test handling of nonexistent input file."""
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file.txt')

def test_invalid_compression_level(sample_file):
    """Test handling of invalid compression levels."""
    with pytest.raises(ValueError):
        compress_file(str(sample_file), compression_level=0)
    
    with pytest.raises(ValueError):
        compress_file(str(sample_file), compression_level=23)

def test_invalid_decompress_file(sample_file):
    """Test handling of invalid decompression input."""
    with pytest.raises(FileNotFoundError):
        decompress_file('/path/to/nonexistent/file.zst')
    
    with pytest.raises(ValueError):
        decompress_file(str(sample_file))  # Not a .zst file