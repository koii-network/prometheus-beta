import pytest
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_lzjb_basic_compression_decompression():
    """Test basic compression and decompression of simple data"""
    original_data = b"Hello, world! This is a test of LZJB compression."
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_repeated_data_compression():
    """Test compression of data with repeated patterns"""
    original_data = b"ABCABCABCABCABCABC" * 10
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_empty_data():
    """Test compression and decompression of empty data"""
    original_data = b""
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) == 0

def test_single_byte_data():
    """Test compression and decompression of single byte data"""
    original_data = b"A"
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data

def test_invalid_input_type():
    """Test that TypeError is raised for non-bytes input"""
    with pytest.raises(TypeError):
        lzjb_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzjb_decompress("not bytes")

def test_binary_data():
    """Test compression of binary data"""
    original_data = bytes(range(256)) * 10
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)