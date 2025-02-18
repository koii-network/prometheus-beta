import pytest
from src.lzss_compression import LZSS

def test_lzss_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"HELLO WORLD! HELLO WORLD!"
    compressed = LZSS.compress(original_data)
    decompressed = LZSS.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_repeated_pattern():
    """Test compression with repeated patterns"""
    original_data = b"ABCABCABCABCABCABC"
    compressed = LZSS.compress(original_data)
    decompressed = LZSS.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_long_data():
    """Test compression with longer input data"""
    original_data = b"This is a test of the LZSS compression algorithm. " * 100
    compressed = LZSS.compress(original_data)
    decompressed = LZSS.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_empty_data():
    """Test compression with empty input"""
    original_data = b""
    compressed = LZSS.compress(original_data)
    decompressed = LZSS.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_string_input():
    """Test compression with string input"""
    original_data = "Hello, world! This is a test of LZSS compression."
    compressed = LZSS.compress(original_data)
    decompressed = LZSS.decompress(compressed)
    
    assert decompressed == original_data.encode('utf-8')

def test_lzss_invalid_compressed_data():
    """Test decompression with invalid compressed data"""
    with pytest.raises(ValueError):
        LZSS.decompress(b'\x00\x01')  # Incomplete compressed data

    with pytest.raises(ValueError):
        LZSS.decompress(b'\x01')  # Incomplete literal data