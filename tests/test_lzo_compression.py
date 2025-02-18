import pytest
import src.lzo_compression as lzo_compression

def test_lzo_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, World! This is a test of LZO compression."
    compressed_data = lzo_compression.lzo_compress(original_data)
    decompressed_data = lzo_compression.lzo_decompress(compressed_data)
    
    assert decompressed_data == original_data

def test_lzo_compression_empty_data():
    """Test compression and decompression with empty data"""
    original_data = b""
    compressed_data = lzo_compression.lzo_compress(original_data)
    decompressed_data = lzo_compression.lzo_decompress(compressed_data)
    
    assert decompressed_data == original_data

def test_lzo_compression_large_data():
    """Test compression and decompression with larger data"""
    original_data = b"a" * 10000
    compressed_data = lzo_compression.lzo_compress(original_data)
    decompressed_data = lzo_compression.lzo_decompress(compressed_data)
    
    assert decompressed_data == original_data

def test_lzo_compression_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzo_compression.lzo_compress("Not bytes")
    
    with pytest.raises(TypeError):
        lzo_compression.lzo_decompress("Not bytes")

def test_lzo_compression_error_handling():
    """Test error handling for invalid compressed data"""
    with pytest.raises(ValueError):
        lzo_compression.lzo_decompress(b"Invalid compressed data")