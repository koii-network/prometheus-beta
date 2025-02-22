import pytest
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_lzjh_compression_basic():
    """Test basic compression and decompression."""
    original_data = b'HELLO WORLD'
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original_data

def test_lzjh_compression_repeated_patterns():
    """Test compression of data with repeated patterns."""
    original_data = b'ABABABABABABAB'
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original_data

def test_lzjh_compression_empty_input():
    """Test compression and decompression of empty input."""
    original_data = b''
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original_data

def test_lzjh_compression_string_input():
    """Test compression with string input."""
    original_data = 'Hello, world!'
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_lzjh_compression_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzjh_compress(123)
    
    with pytest.raises(TypeError):
        lzjh_decompress(123)

def test_lzjh_compression_complex_data():
    """Test compression of complex data with various patterns."""
    original_data = b'the quick brown fox jumps over the lazy dog' * 5
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original_data

def test_compression_ratio():
    """Basic test to ensure some level of compression."""
    original_data = b'ABABABABABABAB' * 100
    compressed = lzjh_compress(original_data)
    assert len(compressed) < len(original_data)