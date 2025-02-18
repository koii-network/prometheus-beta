import pytest
from src.lz78_compression import LZ78Compressor

def test_lz78_compression_simple():
    """Test basic compression and decompression"""
    compressor = LZ78Compressor()
    test_string = "TOBEORNOTTOBEORTOBEORNOT"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Reset compressor for decompression
    decompressor = LZ78Compressor()
    
    # Decompress
    decompressed = decompressor.decompress(compressed)
    
    assert decompressed == test_string

def test_lz78_compression_empty_string():
    """Test compression and decompression of empty string"""
    compressor = LZ78Compressor()
    test_string = ""
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Reset compressor for decompression
    decompressor = LZ78Compressor()
    
    # Decompress
    decompressed = decompressor.decompress(compressed)
    
    assert decompressed == test_string

def test_lz78_compression_repeated_substring():
    """Test compression of string with repeated substrings"""
    compressor = LZ78Compressor()
    test_string = "ABABABABABABABAB"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Reset compressor for decompression
    decompressor = LZ78Compressor()
    
    # Decompress
    decompressed = decompressor.decompress(compressed)
    
    assert decompressed == test_string

def test_lz78_compression_unique_characters():
    """Test compression of string with unique characters"""
    compressor = LZ78Compressor()
    test_string = "ABCDEFGHIJKLMNOP"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Reset compressor for decompression
    decompressor = LZ78Compressor()
    
    # Decompress
    decompressed = decompressor.decompress(compressed)
    
    assert decompressed == test_string