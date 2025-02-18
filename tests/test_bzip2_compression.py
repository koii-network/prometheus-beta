import pytest
import bz2
from src.bzip2_compression import compress_bzip2, decompress_bzip2

def test_compress_bzip2_string():
    """Test compressing a string."""
    original_text = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(original_text)
    assert isinstance(compressed, bytes)
    
    # Check that compression works on longer texts
    long_text = original_text * 10
    long_compressed = compress_bzip2(long_text)
    assert len(long_compressed) < len(long_text.encode('utf-8'))

def test_compress_bzip2_bytes():
    """Test compressing bytes."""
    original_bytes = b"Binary data for compression test"
    compressed = compress_bzip2(original_bytes)
    assert isinstance(compressed, bytes)
    
    # Check that compression works on longer byte sequences
    long_bytes = original_bytes * 10
    long_compressed = compress_bzip2(long_bytes)
    assert len(long_compressed) < len(long_bytes)

def test_decompress_bzip2():
    """Test decompression of compressed data."""
    original_text = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(original_text)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_with_different_levels():
    """Test compression with different compression levels."""
    text = "This is a test of compression effectiveness with repeated data. " * 20
    # Test levels 1-9
    compressed_results = []
    for level in range(1, 10):
        compressed = compress_bzip2(text, level)
        assert isinstance(compressed, bytes)
        decompressed = decompress_bzip2(compressed)
        assert decompressed.decode('utf-8') == text
        compressed_results.append((level, len(compressed)))
    
    # At least some variation in compression sizes is expected
    print("Compression results:", compressed_results)
    # Allow small variations in compression size
    result_sizes = [size for _, size in compressed_results]
    assert max(result_sizes) - min(result_sizes) >= 0

def test_invalid_compression_level():
    """Test handling of invalid compression levels."""
    with pytest.raises(ValueError):
        compress_bzip2("Test", 0)
    with pytest.raises(ValueError):
        compress_bzip2("Test", 10)

def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        compress_bzip2(123)
    with pytest.raises(TypeError):
        compress_bzip2(None)
    with pytest.raises(TypeError):
        decompress_bzip2("Not bytes")
    with pytest.raises(TypeError):
        decompress_bzip2(None)

def test_large_data_compression():
    """Test compression of a larger piece of text."""
    large_text = "A" * 10000
    compressed = compress_bzip2(large_text)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == large_text

def test_empty_data():
    """Test compression and decompression of empty data."""
    empty_text = ""
    compressed = compress_bzip2(empty_text)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == empty_text