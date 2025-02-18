import pytest
from src.lzrw_compression import lzrw_compress, lzrw_decompress

def test_lzrw_compression_simple():
    """Test basic compression and decompression"""
    original = b"Hello, world! This is a test of LZRW compression."
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original

def test_lzrw_compression_repeated_data():
    """Test compression with repeated data"""
    original = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original
    assert len(compressed) < len(original)

def test_lzrw_compression_edge_cases():
    """Test edge cases like empty string and single character"""
    # Empty string
    original_empty = b""
    compressed_empty = lzrw_compress(original_empty)
    decompressed_empty = lzrw_decompress(compressed_empty)
    assert decompressed_empty == original_empty

    # Single character
    original_single = b"A"
    compressed_single = lzrw_compress(original_single)
    decompressed_single = lzrw_decompress(compressed_single)
    assert decompressed_single == original_single

def test_lzrw_compression_string_input():
    """Test compression with string input"""
    original = "Hello, world! This is a test of LZRW compression."
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original.encode('utf-8')

def test_lzrw_compression_complex_data():
    """Test compression with more complex data"""
    original = b"The quick brown fox jumps over the lazy dog. " * 10
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original
    assert len(compressed) < len(original)