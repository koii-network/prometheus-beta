import pytest
from src.huffman_coding import huffman_encode, huffman_decode, build_frequency_dict, build_huffman_tree, build_huffman_codes

def test_build_frequency_dict():
    """Test frequency dictionary creation."""
    data = "hello world"
    freq_dict = build_frequency_dict(data)
    assert freq_dict == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_huffman_encode_decode_simple():
    """Test basic encoding and decoding."""
    data = "hello"
    encoded_data, huffman_codes = huffman_encode(data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == data

def test_huffman_encode_decode_complex():
    """Test encoding and decoding with a more complex string."""
    data = "the quick brown fox jumps over the lazy dog"
    encoded_data, huffman_codes = huffman_encode(data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == data

def test_huffman_edge_cases():
    """Test edge cases for Huffman coding."""
    # Empty string
    assert huffman_encode("") == ("", {})
    assert huffman_decode("", {}) == ""

    # Single character
    single_char_data = "aaaaa"
    encoded, codes = huffman_encode(single_char_data)
    decoded = huffman_decode(encoded, codes)
    assert decoded == single_char_data

def test_invalid_decode():
    """Test decoding with invalid data."""
    with pytest.raises(ValueError):
        huffman_decode("1010101", {'a': '00', 'b': '01'})

def test_unique_codes():
    """Ensure generated Huffman codes are unique."""
    data = "abracadabra"
    _, huffman_codes = huffman_encode(data)
    code_set = set(huffman_codes.values())
    assert len(code_set) == len(huffman_codes)  # No duplicate codes