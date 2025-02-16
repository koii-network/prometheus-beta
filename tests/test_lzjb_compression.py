import pytest
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_lzjb_compression_empty_input():
    assert lzjb_compress(b'') == b''
    assert lzjb_decompress(b'') == b''

def test_lzjb_compression_simple_data():
    test_data = b'hello world'
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == test_data

def test_lzjb_compression_repeated_data():
    test_data = b'aaaaaaaaaabbbbbbbbbb' * 10
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == test_data

def test_lzjb_compression_random_data():
    import os
    test_data = os.urandom(1024)
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == test_data

def test_lzjb_compression_large_data():
    test_data = b'abcdefghijklmnopqrstuvwxyz' * 1000
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    assert decompressed == test_data

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
        assert decompressed == data, f"Failed for input: {data}"