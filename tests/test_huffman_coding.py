import pytest
from src.huffman_coding import (
    build_frequency_dict, 
    build_huffman_tree, 
    build_huffman_codes, 
    huffman_encode, 
    huffman_decode
)

def test_build_frequency_dict():
    data = "hello world"
    freq_dict = build_frequency_dict(data)
    assert freq_dict == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_huffman_encode_decode():
    # Test basic encoding and decoding
    original_data = "hello world"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data

def test_huffman_encode_decode_empty_string():
    # Test empty string
    original_data = ""
    encoded_data, huffman_codes = huffman_encode(original_data)
    assert encoded_data == ""
    assert huffman_codes == {}
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == ""

def test_huffman_encode_decode_single_char():
    # Test single character
    original_data = "a"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data

def test_huffman_codes_uniqueness():
    # Test that generated Huffman codes are unique
    data = "abcdefg"
    _, huffman_codes = huffman_encode(data)
    code_set = set(huffman_codes.values())
    assert len(code_set) == len(huffman_codes)

def test_invalid_decode():
    # Test decoding with invalid encoded data
    with pytest.raises(ValueError):
        huffman_decode("1010101", {'a': '00', 'b': '01'})

def test_complex_data():
    # Test with a more complex string
    original_data = "the quick brown fox jumps over the lazy dog"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data