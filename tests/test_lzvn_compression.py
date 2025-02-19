import pytest
from src.lzvn_compression import LZVNCompressor

def test_lzvn_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! This is a test of LZVN compression."
    compressed = LZVNCompressor.compress(original_data)
    decompressed = LZVNCompressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzvn_repeated_data():
    """Test compression with repeated sequences"""
    repeated_data = b"ABCABCABCABCABCABC" * 10
    compressed = LZVNCompressor.compress(repeated_data)
    decompressed = LZVNCompressor.decompress(compressed)
    
    assert decompressed == repeated_data
    assert len(compressed) < len(repeated_data)

def test_lzvn_edge_cases():
    """Test edge cases like empty input and single byte"""
    # Empty input
    assert LZVNCompressor.compress(b'') == b''
    assert LZVNCompressor.decompress(b'') == b''
    
    # Single byte
    single_byte = b'A'
    compressed = LZVNCompressor.compress(single_byte)
    assert LZVNCompressor.decompress(compressed) == single_byte

def test_lzvn_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        LZVNCompressor.compress("Not bytes")
    
    with pytest.raises(TypeError):
        LZVNCompressor.decompress("Not bytes")

def test_lzvn_binary_data():
    """Test compression with binary data"""
    binary_data = bytes(range(256)) * 5
    compressed = LZVNCompressor.compress(binary_data)
    decompressed = LZVNCompressor.decompress(compressed)
    
    assert decompressed == binary_data