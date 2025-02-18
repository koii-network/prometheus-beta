import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from zstandard_compression import compress_data, decompress_data

def test_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, Zstandard compression!"
    compressed_data = compress_data(original_data)
    decompressed_data = decompress_data(compressed_data)
    
    assert decompressed_data == original_data

def test_string_input():
    """Test compression with string input"""
    original_data = "Testing string compression"
    compressed_data = compress_data(original_data)
    decompressed_data = decompress_data(compressed_data)
    
    assert decompressed_data == original_data.encode('utf-8')

def test_different_compression_levels():
    """Test compression with different levels"""
    data = b"Test data for different compression levels" * 1000  # Increase data size
    
    level_3_compressed = compress_data(data, compression_level=3)
    level_22_compressed = compress_data(data, compression_level=22)
    
    assert len(level_3_compressed) > 0
    assert len(level_22_compressed) > 0
    assert abs(len(level_3_compressed) - len(level_22_compressed)) > 10  # More significant difference

def test_invalid_input_type():
    """Test type validation"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data(123)

def test_invalid_compression_level():
    """Test compression level validation"""
    with pytest.raises(ValueError):
        compress_data(b"test", compression_level=0)
    
    with pytest.raises(ValueError):
        compress_data(b"test", compression_level=23)

def test_empty_data():
    """Test compression and decompression with empty data"""
    empty_data = b""
    compressed_data = compress_data(empty_data)
    decompressed_data = decompress_data(compressed_data)
    
    assert decompressed_data == empty_data