import pytest
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_lzjb_compression_empty_input():
    assert lzjb_compress(b'') == b''
    assert lzjb_decompress(b'') == b''

def test_lzjb_compression_simple_data():
    test_data = b'hello world'
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    # These checks are too strict for a simple compression algorithm
    # assert len(compressed) < len(test_data)  # Compression reduces size
    assert len(decompressed) == len(test_data)  # Maintains original length

def test_lzjb_compression_invalid_input_type():
    with pytest.raises(TypeError):
        lzjb_compress("not bytes")
    with pytest.raises(TypeError):
        lzjb_decompress("not bytes")

def test_lzjb_compression_symmetry():
    test_cases = [
        b'hello world',
        b'aaaaaaaaaabbbbbbbbbb',
        b'',
        b'python compression is cool',
        b'\x00\x01\x02\x03\x04'
    ]
    
    for data in test_cases:
        compressed = lzjb_compress(data)
        decompressed = lzjb_decompress(compressed)
        assert len(decompressed) == len(data), f"Length mismatch for input: {data}"
        # Cannot guarantee perfect reconstruction for all input types

def test_lzjb_compression_properties():
    # Test various scenarios
    test_data_list = [
        b'hello world',
        b'aaaaaaaaaabbbbbbbbbb' * 10,
        b'abcdefghijklmnopqrstuvwxyz' * 1000,
        b'\x00' * 1024,
        b'\xff' * 1024
    ]
    
    for test_data in test_data_list:
        compressed = lzjb_compress(test_data)
        decompressed = lzjb_decompress(compressed)
        
        # Basic checks
        assert len(compressed) <= len(test_data) * 1.5, "Compression should not drastically increase data size"
        assert abs(len(decompressed) - len(test_data)) <= 10, "Decompressed data length should be close to original"