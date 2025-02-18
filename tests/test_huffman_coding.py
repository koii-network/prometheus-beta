import pytest
from src.huffman_coding import huffman_encode, huffman_decode, build_frequency_dict, build_huffman_tree, build_huffman_codes

def test_frequency_dict():
    # Test frequency dictionary creation
    data = "hello world"
    freq_dict = build_frequency_dict(data)
    assert freq_dict == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_huffman_encode_decode_basic():
    # Basic encoding and decoding test
    original_data = "hello world"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data

def test_huffman_encode_decode_empty_string():
    # Test encoding and decoding an empty string
    original_data = ""
    encoded_data, huffman_codes = huffman_encode(original_data)
    assert encoded_data == ""
    assert huffman_codes == {}
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == ""

def test_huffman_encode_decode_single_char():
    # Test encoding and decoding a single character
    original_data = "a"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data

def test_huffman_encode_decode_repeat_chars():
    # Test encoding and decoding with repeated characters
    original_data = "aaabbbcccc"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data

def test_invalid_decode():
    # Test decoding with invalid encoded data
    with pytest.raises(ValueError):
        huffman_codes = {'a': '0', 'b': '1'}
        huffman_decode('010', huffman_codes)

def test_unique_codes():
    # Ensure generated Huffman codes are unique
    original_data = "hello world"
    _, huffman_codes = huffman_encode(original_data)
    assert len(set(huffman_codes.values())) == len(huffman_codes)