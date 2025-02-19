import pytest
import zlib

# Import the functions to test
from src.deflate_compression import deflate_compress, deflate_decompress

def test_deflate_compression_basic():
    """Test basic compression and decompression"""
    original_text = "Hello, Deflate compression!"
    compressed = deflate_compress(original_text)
    
    # Check that compression returns bytes and reduces size
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_text.encode('utf-8'))
    
    # Verify decompression works
    decompressed = deflate_decompress(compressed)
    assert decompressed == original_text

def test_deflate_compression_levels():
    """Test different compression levels"""
    text = "This is a test string for compression levels"
    
    # Test various compression levels
    for level in range(10):
        compressed = deflate_compress(text, level)
        decompressed = deflate_decompress(compressed)
        assert decompressed == text

def test_deflate_empty_string():
    """Test compression and decompression of an empty string"""
    empty_string = ""
    compressed = deflate_compress(empty_string)
    decompressed = deflate_decompress(compressed)
    assert decompressed == empty_string

def test_deflate_long_string():
    """Test compression of a longer string"""
    long_text = "A" * 10000
    compressed = deflate_compress(long_text)
    decompressed = deflate_decompress(compressed)
    assert decompressed == long_text

def test_deflate_invalid_input_types():
    """Test error handling for invalid input types"""
    # Test non-string input for compression
    with pytest.raises(TypeError):
        deflate_compress(123)
    
    # Test non-bytes input for decompression
    with pytest.raises(TypeError):
        deflate_decompress("not bytes")

def test_deflate_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    text = "Compression level test"
    
    # Test levels outside valid range
    with pytest.raises(ValueError):
        deflate_compress(text, -1)
    
    with pytest.raises(ValueError):
        deflate_compress(text, 10)

def test_deflate_invalid_compressed_data():
    """Test error handling for invalid compressed data"""
    # Try to decompress invalid bytes
    with pytest.raises(zlib.error):
        deflate_decompress(b'Invalid compressed data')