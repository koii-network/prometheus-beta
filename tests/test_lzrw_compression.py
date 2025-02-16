import pytest
from src.lzrw_compression import lzrw_compress, lzrw_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, World! This is a test of LZRW compression."
    compressed = lzrw_compress(original_data)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original_data

def test_repeated_sequence_compression():
    """Test compression of data with repeated sequences"""
    original_data = b"ABCABCABCABCABCABC" * 10
    compressed = lzrw_compress(original_data)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original_data

def test_empty_input():
    """Test compression and decompression of empty input"""
    original_data = b""
    compressed = lzrw_compress(original_data)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original_data

def test_single_byte_input():
    """Test compression and decompression of single byte"""
    original_data = b"A"
    compressed = lzrw_compress(original_data)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original_data

def test_binary_data():
    """Test compression of binary data"""
    original_data = bytes(range(256)) * 3
    compressed = lzrw_compress(original_data)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original_data

def test_large_input():
    """Test compression of larger input"""
    original_data = b"Test data " * 1000
    compressed = lzrw_compress(original_data)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original_data

def test_compression_reduces_size():
    """Verify that compression reduces the size of the input"""
    original_data = b"ABCABCABCABCABCABC" * 100
    compressed = lzrw_compress(original_data)
    
    assert len(compressed) < len(original_data)