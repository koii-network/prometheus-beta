import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzvn_compression import lzvn_compress, lzvn_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"HELLO WORLD! HELLO WORLD! HELLO WORLD!"
    
    # Compress
    compressed = lzvn_compress(original_data)
    assert compressed is not None
    assert len(compressed) < len(original_data)
    
    # Decompress
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original_data

def test_repeated_pattern():
    """Test compression of data with repeated patterns"""
    repeated_data = b"ABCABCABCABCABCABC" * 10
    
    # Compress
    compressed = lzvn_compress(repeated_data)
    assert compressed is not None
    assert len(compressed) < len(repeated_data)
    
    # Decompress
    decompressed = lzvn_decompress(compressed)
    assert decompressed == repeated_data

def test_random_data():
    """Test compression of random data"""
    import random
    random.seed(42)  # for reproducibility
    random_data = bytes(random.randint(0, 255) for _ in range(1000))
    
    # Compress
    compressed = lzvn_compress(random_data)
    
    # Decompress
    decompressed = lzvn_decompress(compressed)
    assert decompressed == random_data

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_data = b""
    
    # Compress
    compressed = lzvn_compress(empty_data)
    assert compressed == b""
    
    # Decompress
    decompressed = lzvn_decompress(compressed)
    assert decompressed == b""

def test_large_data():
    """Test compression of larger data"""
    large_data = b"TEST DATA" * 10000
    
    # Compress
    compressed = lzvn_compress(large_data)
    assert compressed is not None
    assert len(compressed) < len(large_data)
    
    # Decompress
    decompressed = lzvn_decompress(compressed)
    assert decompressed == large_data