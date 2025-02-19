import pytest
from src.lzh_compression import LZHCompressor

def test_lzh_compression_basic():
    """Test basic compression and decompression of a simple string"""
    compressor = LZHCompressor()
    original_data = "HELLO WORLD"
    
    # Compress
    compressed, huffman_codes = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed, huffman_codes)
    
    assert decompressed == original_data

def test_lzh_compression_repeated_patterns():
    """Test compression with repeated patterns"""
    compressor = LZHCompressor()
    original_data = "ABABABABABABABAB"
    
    # Compress
    compressed, huffman_codes = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed, huffman_codes)
    
    assert decompressed == original_data

def test_lzh_compression_empty_string():
    """Test compression and decompression of an empty string"""
    compressor = LZHCompressor()
    original_data = ""
    
    # Compress
    compressed, huffman_codes = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed, huffman_codes)
    
    assert decompressed == original_data

def test_lzh_compression_long_string():
    """Test compression of a longer string with various patterns"""
    compressor = LZHCompressor()
    original_data = "This is a test of the LZH compression algorithm. " * 10
    
    # Compress
    compressed, huffman_codes = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed, huffman_codes)
    
    assert decompressed == original_data

def test_lzh_compression_special_characters():
    """Test compression with special characters and mixed content"""
    compressor = LZHCompressor()
    original_data = "Hello, World! 123 @#$ %^& *()_+"
    
    # Compress
    compressed, huffman_codes = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed, huffman_codes)
    
    assert decompressed == original_data