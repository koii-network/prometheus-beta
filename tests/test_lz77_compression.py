import pytest
from src.lz77_compression import LZ77Compressor

def test_lz77_compressor_basic():
    """Test basic compression and decompression"""
    compressor = LZ77Compressor()
    test_string = "ABABABABABABABAB"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_lz77_compressor_repeated_pattern():
    """Test compression with repeated patterns"""
    compressor = LZ77Compressor()
    test_string = "Hello, hello, hello, world!"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_lz77_compressor_long_text():
    """Test compression with longer text"""
    compressor = LZ77Compressor()
    test_string = "a" * 100 + "b" * 50 + "a" * 100
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_lz77_compressor_empty_string():
    """Test compression with empty string"""
    compressor = LZ77Compressor()
    test_string = ""
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_lz77_compressor_bytes():
    """Test compression with byte input"""
    compressor = LZ77Compressor()
    test_bytes = b"Hello, world! Hello, world!"
    
    # Compress
    compressed = compressor.compress(test_bytes)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed == test_bytes