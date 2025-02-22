import pytest
from src.lzvn_compression import lzvn_compress, lzvn_decompress

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_data = b''
    assert lzvn_compress(empty_data) == b''
    assert lzvn_decompress(b'') == b''

def test_simple_compression():
    """Test basic compression and decompression"""
    test_data = b'Hello, world! Hello, world!'
    compressed = lzvn_compress(test_data)
    assert compressed != test_data
    assert lzvn_decompress(compressed) == test_data

def test_repeated_patterns():
    """Test compression of data with repeated patterns"""
    test_data = b'ABCABCABCABC' * 10
    compressed = lzvn_compress(test_data)
    assert len(compressed) < len(test_data)
    assert lzvn_decompress(compressed) == test_data

def test_binary_data():
    """Test compression of binary data"""
    test_data = bytes(range(256)) * 10
    compressed = lzvn_compress(test_data)
    assert lzvn_decompress(compressed) == test_data

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        lzvn_compress("not bytes")
    with pytest.raises(TypeError):
        lzvn_decompress("not bytes")

def test_roundtrip_compression():
    """Comprehensive roundtrip compression test"""
    test_cases = [
        b'Short text',
        b'Repeated data ' * 100,
        bytes(range(128)),
        b'\x00' * 50 + b'\xFF' * 50
    ]
    
    for test_data in test_cases:
        compressed = lzvn_compress(test_data)
        decompressed = lzvn_decompress(compressed)
        assert decompressed == test_data, f"Failed for test data: {test_data}"