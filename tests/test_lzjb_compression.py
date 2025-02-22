import pytest
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_simple_compression_decompression():
    """Test basic compression and decompression of a simple string."""
    original_data = b"Hello, world! This is a test of LZJB compression."
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_repeated_data_compression():
    """Test compression of data with many repetitions."""
    original_data = b"ABCABCABCABCABCABCABCABC" * 10
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_empty_data():
    """Test compression and decompression of empty data."""
    original_data = b""
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) == 0

def test_single_byte_data():
    """Test compression and decompression of single byte data."""
    original_data = b"A"
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data

def test_large_data():
    """Test compression and decompression of larger data."""
    original_data = b"0123456789" * 1000
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_binary_data():
    """Test compression and decompression of binary data."""
    original_data = bytes([x % 256 for x in range(256)] * 10)
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data