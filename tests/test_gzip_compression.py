import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gzip_compression import compress_data, decompress_data

def test_compress_and_decompress_string():
    # Test compression and decompression of a string
    original_data = "Hello, world! This is a test of Gzip compression."
    compressed = compress_data(original_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_compress_and_decompress_bytes():
    # Test compression and decompression of bytes
    original_data = b"Binary data compression test"
    compressed = compress_data(original_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed == original_data

def test_compress_invalid_input_type():
    # Test compression with invalid input type
    with pytest.raises(TypeError):
        compress_data(12345)
    with pytest.raises(TypeError):
        compress_data(None)
    with pytest.raises(TypeError):
        compress_data(["list"])

def test_decompress_invalid_input_type():
    # Test decompression with invalid input type
    with pytest.raises(TypeError):
        decompress_data("not bytes")
    with pytest.raises(TypeError):
        decompress_data(12345)

def test_empty_input():
    # Test empty input for both compress and decompress
    with pytest.raises(ValueError):
        compress_data("")
    with pytest.raises(ValueError):
        decompress_data(b"")

def test_invalid_gzip_data():
    # Test decompression of invalid Gzip data
    with pytest.raises(ValueError):
        decompress_data(b"Invalid Gzip data")

def test_large_data_compression():
    # Test compression and decompression of a large string
    large_data = "A" * 10000
    compressed = compress_data(large_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == large_data
    assert len(compressed) < len(large_data)