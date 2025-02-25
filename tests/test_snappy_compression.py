import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import compress_snappy, decompress_snappy

def test_basic_compression_decompression():
    """Test basic compression and decompression of a string."""
    original_data = "Hello, Snappy compression!"
    compressed = compress_snappy(original_data)
    decompressed = decompress_snappy(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_binary_data_compression():
    """Test compression and decompression of binary data."""
    original_data = b'\x00\x01\x02\x03\xff\xfe\xfd'
    compressed = compress_snappy(original_data)
    decompressed = decompress_snappy(compressed)
    
    assert decompressed == original_data

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_snappy(b'')
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        decompress_snappy(b'')

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_snappy(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        decompress_snappy(123)

def test_large_data_compression():
    """Test compression and decompression of a large piece of data."""
    original_data = "This is a large text " * 1000
    compressed = compress_snappy(original_data)
    decompressed = decompress_snappy(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_invalid_compressed_data():
    """Test that invalid compressed data raises an error."""
    with pytest.raises(ValueError, match="Invalid compressed data"):
        decompress_snappy(b'InvalidCompressedData')