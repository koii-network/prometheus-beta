import pytest
from src.lz77_compression import LZ77Compressor

def test_lz77_compressor_empty_input():
    """Test compression and decompression of empty input"""
    compressor = LZ77Compressor()
    input_data = ""
    compressed = compressor.compress(input_data)
    assert compressed == []
    assert compressor.decompress(compressed) == b''

def test_lz77_compressor_simple_text():
    """Test compression and decompression of simple text"""
    compressor = LZ77Compressor()
    input_data = "AAAAABBBBBCCCCC"
    compressed = compressor.compress(input_data)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_lz77_compressor_repeated_pattern():
    """Test compression of text with repeated patterns"""
    compressor = LZ77Compressor()
    input_data = "Hello hello hello world world world"
    compressed = compressor.compress(input_data)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_lz77_compressor_bytes_input():
    """Test compression and decompression of byte input"""
    compressor = LZ77Compressor()
    input_data = b'\x00\x01\x02\x00\x01\x02\x03\x04'
    compressed = compressor.compress(input_data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == input_data

def test_lz77_compressor_different_window_sizes():
    """Test compression with different window sizes"""
    test_data = "This is a test of compression with different window sizes and repeated patterns"
    
    for window_size in [128, 256, 512, 1024]:
        compressor = LZ77Compressor(window_size=window_size)
        compressed = compressor.compress(test_data)
        decompressed = compressor.decompress(compressed)
        assert decompressed.decode('utf-8') == test_data

def test_lz77_compressor_error_handling():
    """Test error handling for invalid inputs"""
    compressor = LZ77Compressor()
    
    # Test with None input
    with pytest.raises(TypeError):
        compressor.compress(None)
    
    # Test with non-string/bytes input
    with pytest.raises(TypeError):
        compressor.compress(12345)