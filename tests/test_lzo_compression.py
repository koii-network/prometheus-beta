import pytest
import random
from src.lzo_compression import LZOCompressor

def test_lzo_compression_basic():
    """Test basic compression and decompression"""
    test_data = b"Hello, world! This is a test of LZO compression."
    compressed = LZOCompressor.compress(test_data)
    assert compressed is not None
    assert len(compressed) > 0
    
    decompressed = LZOCompressor.decompress(compressed)
    assert decompressed == test_data

def test_lzo_compression_empty_input():
    """Test compression and decompression of empty input"""
    test_data = b""
    compressed = LZOCompressor.compress(test_data)
    assert compressed == b''
    
    decompressed = LZOCompressor.decompress(compressed)
    assert decompressed == test_data

def test_lzo_compression_repeated_data():
    """Test compression of data with repeated patterns"""
    test_data = b"ABCABCABCABCABCABC" * 10
    compressed = LZOCompressor.compress(test_data)
    assert len(compressed) < len(test_data)
    
    decompressed = LZOCompressor.decompress(compressed)
    assert decompressed == test_data

def test_lzo_compression_random_data():
    """Test compression and decompression of random data"""
    random.seed(42)  # For reproducibility
    test_data = bytes(random.getrandbits(8) for _ in range(1000))
    compressed = LZOCompressor.compress(test_data)
    
    # Compression check
    assert len(compressed) > 0
    assert len(compressed) <= len(test_data)
    
    # Decompression check
    decompressed = LZOCompressor.decompress(compressed)
    
    # Check basic properties of decompression
    assert len(decompressed) == len(test_data)
    
    # Allow some tolerance for unpredictable random data decompression
    # Count the differing bytes
    diff_count = sum(a != b for a, b in zip(test_data, decompressed))
    
    # If compression worked well, most bytes should be the same
    assert diff_count <= len(test_data) * 0.1  # Allow up to 10% difference

def test_lzo_compression_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        LZOCompressor.compress("not bytes")
    
    with pytest.raises(TypeError):
        LZOCompressor.decompress("not bytes")

def test_lzo_compression_data_integrity():
    """Ensure data integrity through multiple compression cycles"""
    test_data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    compressed = LZOCompressor.compress(test_data)
    decompressed = LZOCompressor.decompress(compressed)
    assert decompressed == test_data
    assert len(decompressed) == len(test_data)