import pytest
from src.lzh_compression import lzh_compress, build_frequency_dict, build_huffman_codes, build_huffman_tree

def test_lzh_compress_empty_string():
    result = lzh_compress('')
    assert result == {'compressed_data': '', 'huffman_codes': {}}

def test_lzh_compress_simple_string():
    result = lzh_compress('ABRACADABRA')
    assert 'compressed_data' in result
    assert 'huffman_codes' in result
    assert isinstance(result['compressed_data'], str)
    assert isinstance(result['huffman_codes'], dict)

def test_lzh_compress_repeated_pattern():
    result = lzh_compress('AAAAAAAA')
    assert result['compressed_data']  # Should not be empty
    assert 'A' in result['huffman_codes']

def test_lzh_compress_bytes_input():
    result = lzh_compress(b'Hello, World!')
    assert result['compressed_data']
    assert isinstance(result['compressed_data'], str)

def test_build_frequency_dict():
    freq = build_frequency_dict('ABRACADABRA')
    assert freq['A'] == 5
    assert freq['B'] == 2
    assert freq['R'] == 2
    assert freq['C'] == 1
    assert freq['D'] == 1

def test_huffman_codes():
    freq = build_frequency_dict('HELLO')
    tree = build_huffman_tree(freq)
    codes = build_huffman_codes(tree)
    assert set(codes.keys()) == set('HELO')
    assert all(len(code) > 0 for code in codes.values())

def test_compression_length():
    original = 'ABRACADABRA' * 10
    result = lzh_compress(original)
    assert len(result['compressed_data']) < len(original) * 8  # Compressed data should be shorter