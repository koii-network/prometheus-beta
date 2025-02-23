import pytest
from src.huffman_coding import huffman_encode, huffman_decode, build_frequency_dict, build_huffman_tree, build_huffman_codes

def test_build_frequency_dict():
    data = "hello world"
    freq_dict = build_frequency_dict(data)
    expected = {
        'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1
    }
    assert freq_dict == expected

def test_huffman_encode_decode_simple():
    data = "hello"
    encoded_data, huffman_codes = huffman_encode(data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == data

def test_huffman_encode_decode_complex():
    data = "The quick brown fox jumps over the lazy dog"
    encoded_data, huffman_codes = huffman_encode(data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == data

def test_huffman_encode_empty_string():
    data = ""
    encoded_data, huffman_codes = huffman_encode(data)
    assert encoded_data == ""
    assert huffman_codes == {}

def test_huffman_decode_empty_string():
    encoded_data = ""
    huffman_codes = {}
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == ""

def test_invalid_encoded_data():
    with pytest.raises(ValueError):
        huffman_decode("10101", {"0": "A", "1": "B"})

def test_single_character_string():
    data = "aaaaa"
    encoded_data, huffman_codes = huffman_encode(data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == data

def test_mixed_character_types():
    data = "Hello, ä¸ç!"
    encoded_data, huffman_codes = huffman_encode(data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == data