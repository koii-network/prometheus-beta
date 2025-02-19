import pytest
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_lzjh_compression_basic():
    """Test basic compression and decompression"""
    original_data = b'HELLO WORLD'
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original_data

def test_lzjh_compression_repeated_sequence():
    """Test compression of repeated sequences"""
    original_data = b'AAAAAAAAAA'
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original_data

def test_lzjh_compression_empty_input():
    """Test compression of empty input"""
    original_data = b''
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original_data

def test_lzjh_compression_mixed_data():
    """Test compression of mixed data"""
    original_data = b'abcabcabcabcabc'
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original_data

def test_lzjh_compression_large_input():
    """Test compression of a larger input"""
    original_data = b'This is a longer test string with some repeated sequences to test the compression algorithm more thoroughly.'
    compressed = lzjh_compress(original_data)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original_data