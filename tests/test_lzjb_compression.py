"""
Test suite for LZJB compression and decompression functions
"""

import pytest
import random
from src.lzjb_compression import compress, decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! This is a test of LZJB compression."
    compressed = compress(original_data)
    decompressed = decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) <= len(original_data)

def test_repeated_data_compression():
    """Test compression of data with repeated patterns"""
    original_data = b"abcabcabcabcabcabcabcabcabcabc" * 10
    compressed = compress(original_data)
    decompressed = decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_large_random_data():
    """Test compression of large random data"""
    # Generate 10KB of random data
    random.seed(42)  # For reproducibility
    original_data = bytes(random.getrandbits(8) for _ in range(10 * 1024))
    
    compressed = compress(original_data)
    decompressed = decompress(compressed)
    
    assert decompressed == original_data

def test_edge_cases():
    """Test edge cases and error handling"""
    # Single byte
    single_byte = b'A'
    assert decompress(compress(single_byte)) == single_byte
    
    # Empty input should raise ValueError
    with pytest.raises(ValueError):
        compress(b'')
    
    with pytest.raises(ValueError):
        decompress(b'')
    
    # Invalid input type
    with pytest.raises(TypeError):
        compress("not bytes")
    
    with pytest.raises(TypeError):
        decompress("not bytes")

def test_compression_ratio():
    """Test that compression provides some size reduction"""
    # Use a string with repetitive patterns
    original_data = b"COMPRESSCOMPRESSCOMPRESSCOMPRESS" * 100
    
    compressed = compress(original_data)
    decompressed = decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_complex_patterns():
    """Test compression with more complex repeated patterns"""
    original_data = (
        b"The quick brown fox jumps over the lazy dog. " * 20 +
        b"Pack my box with five dozen liquor jugs." * 10
    )
    
    compressed = compress(original_data)
    decompressed = decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) <= len(original_data)