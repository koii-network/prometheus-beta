import pytest
from src.lzrw_compression import lzrw_compress, lzrw_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original = b"Hello, world! This is a test of LZRW compression."
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original

def test_empty_input():
    """Test compression and decompression of empty input"""
    original = b""
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original

def test_repeated_pattern():
    """Test compression of repeated patterns"""
    original = b"AAAAAAAAABBBBBBBBBCCCCCCCCCC"
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original
    assert len(compressed) < len(original)

def test_non_compressible_data():
    """Test compression of random or non-compressible data"""
    original = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original

def test_unicode_string():
    """Test compression with unicode string"""
    original = "Hello, 世界! This is a Unicode test.".encode('utf-8')
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original

def test_large_input():
    """Test compression of a larger input"""
    original = b"This is a longer text with some repeating patterns " * 100
    compressed = lzrw_compress(original)
    decompressed = lzrw_decompress(compressed)
    
    assert decompressed == original
    assert len(compressed) < len(original)

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(ValueError):
        lzrw_decompress(b'\xFF\xFF\xFF')  # Invalid codes

def test_compression_ratio():
    """Verify that compression reduces data size for repetitive input"""
    original = b"ABCDEFG" * 1000
    compressed = lzrw_compress(original)
    
    assert len(compressed) < len(original)