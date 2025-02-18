import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_data_str():
    """Test compression with string input"""
    original_data = "Hello, world!"
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data.encode('utf-8'))

def test_compress_data_bytes():
    """Test compression with bytes input"""
    original_data = b"Hello, world!"
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data)

def test_decompress_data():
    """Test decompression of compressed data"""
    original_data = "Hello, world!"
    compressed = compress_data(original_data)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_compress_decompress_cycle():
    """Test full compression and decompression cycle"""
    test_cases = [
        "Hello, world!",
        "This is a longer test string with more content.",
        b"Binary data test",
        b"\x00\x01\x02\x03\x04"
    ]
    
    for data in test_cases:
        compressed = compress_data(data)
        decompressed = decompress_data(compressed)
        
        if isinstance(data, str):
            assert decompressed.decode('utf-8') == data
        else:
            assert decompressed == data

def test_compression_levels():
    """Test different compression levels"""
    data = "Test compression levels"
    
    compressed_levels = [compress_data(data, level) for level in range(10)]
    
    # Verify different levels produce different compressed sizes
    sizes = [len(compressed) for compressed in compressed_levels]
    assert len(set(sizes)) > 1

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("test", -1)
    
    with pytest.raises(ValueError):
        compress_data("test", 10)

def test_decompression_error():
    """Test error handling for invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b"invalid compressed data")