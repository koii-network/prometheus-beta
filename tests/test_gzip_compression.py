import pytest
import gzip
import src.gzip_compression as gzip_compression

def test_gzip_compress_string():
    """Test compressing a string"""
    input_str = "Hello, world! This is a test of Gzip compression."
    compressed = gzip_compression.gzip_compress(input_str)
    
    # Verify it's a valid gzip compressed file
    assert compressed[0:2] == b'\x1f\x8b'  # Gzip magic number
    
    # Verify we can decompress back to original
    decompressed = gzip.decompress(compressed).decode('utf-8')
    assert decompressed == input_str

def test_gzip_compress_bytes():
    """Test compressing bytes"""
    input_bytes = b"Binary data to compress"
    compressed = gzip_compression.gzip_compress(input_bytes)
    
    # Verify it's a valid gzip compressed file
    assert compressed[0:2] == b'\x1f\x8b'  # Gzip magic number
    
    # Verify we can decompress back to original
    decompressed = gzip.decompress(compressed)
    assert decompressed == input_bytes

def test_gzip_compress_compression_levels():
    """Test different compression levels"""
    input_data = "Compression level test" * 100  # Longer text to show differences
    
    # Test various compression levels
    for level in range(10):
        compressed = gzip_compression.gzip_compress(input_data, compression_level=level)
        decompressed = gzip.decompress(compressed).decode('utf-8')
        assert decompressed == input_data

def test_gzip_compress_invalid_compression_level():
    """Test invalid compression levels"""
    with pytest.raises(ValueError, match="Compression level must be between 0 and 9"):
        gzip_compression.gzip_compress("test", compression_level=10)
    
    with pytest.raises(ValueError, match="Compression level must be between 0 and 9"):
        gzip_compression.gzip_compress("test", compression_level=-1)

def test_gzip_compress_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be str or bytes"):
        gzip_compression.gzip_compress(123)
    
    with pytest.raises(TypeError, match="Input must be str or bytes"):
        gzip_compression.gzip_compress(None)

def test_gzip_compress_empty_input():
    """Test compressing empty input"""
    empty_str = ""
    empty_bytes = b""
    
    compressed_str = gzip_compression.gzip_compress(empty_str)
    compressed_bytes = gzip_compression.gzip_compress(empty_bytes)
    
    # Both should decompress to empty
    assert gzip.decompress(compressed_str) == b''
    assert gzip.decompress(compressed_bytes) == b''