import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from huffman_coding import huffman_encode, huffman_decode, build_frequency_dict, build_huffman_tree, build_huffman_codes

def test_build_frequency_dict():
    """Test building frequency dictionary"""
    test_str = "hello world"
    freq_dict = build_frequency_dict(test_str)
    expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    assert freq_dict == expected

def test_build_frequency_dict_empty():
    """Test frequency dictionary with empty string"""
    assert build_frequency_dict('') == {}

def test_huffman_encode_basic():
    """Test basic Huffman encoding"""
    test_str = "hello"
    encoded_data, huffman_codes = huffman_encode(test_str)
    
    # Verify we have codes for each character
    assert set(huffman_codes.keys()) == set('helo')
    
    # Verify decoding returns original string
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == test_str

def test_huffman_encode_decode_complex():
    """Test encoding and decoding with a more complex string"""
    test_str = "the quick brown fox jumps over the lazy dog"
    encoded_data, huffman_codes = huffman_encode(test_str)
    
    # Verify decoding returns original string
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == test_str

def test_huffman_encode_empty():
    """Test encoding an empty string"""
    encoded_data, huffman_codes = huffman_encode('')
    assert encoded_data == ''
    assert huffman_codes == {}

def test_huffman_decode_empty():
    """Test decoding an empty string"""
    assert huffman_decode('', {}) == ''

def test_huffman_decode_invalid():
    """Test decoding with invalid encoded data"""
    with pytest.raises(ValueError):
        huffman_decode('1010101', {'0': 'a', '1': 'b'})

def test_build_huffman_tree():
    """Test building a Huffman tree"""
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    tree_root = build_huffman_tree(freq_dict)
    
    # Verify tree is built correctly
    assert tree_root is not None
    assert tree_root.freq == sum(freq_dict.values())

def test_build_huffman_codes():
    """Test generating Huffman codes"""
    freq_dict = {'a': 5, 'b': 9, 'c': 12}
    tree_root = build_huffman_tree(freq_dict)
    huffman_codes = build_huffman_codes(tree_root)
    
    # Verify codes are generated and unique
    assert set(huffman_codes.keys()) == set('abc')
    assert len(set(huffman_codes.values())) == 3  # Unique codes