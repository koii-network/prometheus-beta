import pytest
from src.lzrw_compression import lzrw_compress, lzrw_decompress

def test_empty_input():
    """Test compression and decompression of empty input."""
    empty_data = b''
    assert lzrw_compress(empty_data) == b''
    assert lzrw_decompress(lzrw_compress(empty_data)) == b''

def test_simple_compression():
    """Test basic compression and decompression."""
    data = b'hello world hello world'
    compressed = lzrw_compress(data)
    assert compressed != data
    assert lzrw_decompress(compressed) == data

def test_repeated_pattern():
    """Test compression of repeated patterns."""
    data = b'AAAAAAAAAABBBBBBBBBB' * 10
    compressed = lzrw_compress(data)
    assert len(compressed) < len(data)
    assert lzrw_decompress(compressed) == data

def test_binary_data():
    """Test compression of binary data."""
    data = bytes(range(256)) * 3
    compressed = lzrw_compress(data)
    assert lzrw_decompress(compressed) == data

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzrw_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzrw_decompress("not bytes")

def test_no_compression_case():
    """Test case with minimal or no compression opportunities."""
    data = b'abcdefghijklmnopqrstuvwxyz'
    compressed = lzrw_compress(data)
    assert lzrw_decompress(compressed) == data

def test_large_input():
    """Test compression of a larger input."""
    data = b'test ' * 10000
    compressed = lzrw_compress(data)
    assert len(compressed) < len(data)
    assert lzrw_decompress(compressed) == data