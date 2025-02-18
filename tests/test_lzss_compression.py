import pytest
from src.lzss_compression import LZSSCompressor

def test_lzss_compression_empty_input():
    """Test compression and decompression of empty input"""
    compressor = LZSSCompressor()
    data = b''
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lzss_compression_short_string():
    """Test compression and decompression of a short string"""
    compressor = LZSSCompressor()
    data = "Hello, World!"
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == data

def test_lzss_compression_repeated_data():
    """Test compression of data with repeated patterns"""
    compressor = LZSSCompressor()
    data = "AAAAAAAAAAAAAAAA"  # Repeated pattern
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == data
    assert len(compressed) < len(data)

def test_lzss_compression_random_bytes():
    """Test compression of random bytes"""
    compressor = LZSSCompressor()
    data = bytes(range(256)) * 10  # Repeating byte sequence
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lzss_compression_large_input():
    """Test compression of a larger input"""
    compressor = LZSSCompressor()
    data = "This is a test of the LZSS compression algorithm. " * 100
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == data

def test_lzss_custom_window_size():
    """Test compression with a custom window size"""
    compressor = LZSSCompressor(window_size=1024, look_ahead_size=32)
    data = "Repeated data to test custom window size. " * 50
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == data

def test_lzss_error_handling():
    """Test error handling for invalid compressed data"""
    compressor = LZSSCompressor()
    
    # Test invalid flag
    with pytest.raises(ValueError):
        compressor.decompress(bytes([2, 3, 4]))
    
    # Test incomplete match data
    with pytest.raises(IndexError):
        compressor.decompress(bytes([0, 1]))