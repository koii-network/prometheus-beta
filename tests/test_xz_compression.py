import os
import pytest
import lzma
from src.xz_compression import compress_xz, decompress_xz

def test_compress_xz_string():
    """Test XZ compression with a string input"""
    test_string = "Hello, world! This is a test of XZ compression."
    compressed = compress_xz(test_string)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_string.encode('utf-8')

def test_compress_xz_bytes():
    """Test XZ compression with bytes input"""
    test_bytes = b"Hello, world! This is a test of XZ compression."
    compressed = compress_xz(test_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_bytes

def test_xz_compression_decompression():
    """Test full compression and decompression cycle"""
    test_string = "Hello, world! This is a test of XZ compression and decompression."
    compressed = compress_xz(test_string)
    decompressed = decompress_xz(compressed)
    assert decompressed.decode('utf-8') == test_string

def test_xz_compression_file():
    """Test compressing to a file"""
    test_string = "Test file compression"
    output_path = "temp/compressed.xz"
    
    # Ensure temp directory exists
    os.makedirs("temp", exist_ok=True)
    
    # Compress to file
    compress_xz(test_string, output_path)
    
    # Check file exists and is not empty
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0
    
    # Decompress and verify
    decompressed = decompress_xz(output_path)
    assert decompressed.decode('utf-8') == test_string
    
    # Clean up
    os.remove(output_path)
    os.rmdir("temp")

def test_compression_levels():
    """Test different compression levels"""
    test_string = "Test compression levels"
    
    # Test valid compression levels
    for level in range(10):
        compressed = compress_xz(test_string, compression_level=level)
        assert isinstance(compressed, bytes)
        assert len(compressed) > 0

def test_invalid_compression_level():
    """Test invalid compression levels"""
    test_string = "Test invalid compression level"
    
    # Test below 0
    with pytest.raises(ValueError):
        compress_xz(test_string, compression_level=-1)
    
    # Test above 9
    with pytest.raises(ValueError):
        compress_xz(test_string, compression_level=10)

def test_decompress_invalid_data():
    """Test decompression of invalid data"""
    with pytest.raises(lzma.LZMAError):
        decompress_xz(b"Invalid compressed data")