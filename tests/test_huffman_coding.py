import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.huffman_coding import (
    build_frequency_dict, 
    build_huffman_tree, 
    build_huffman_codes, 
    compress, 
    decompress,
    HuffmanNode
)

def test_build_frequency_dict():
    """Test frequency dictionary creation"""
    input_str = "hello world"
    freq_dict = build_frequency_dict(input_str)
    assert freq_dict == {
        'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1
    }
    
    # Test empty string
    assert build_frequency_dict("") == {}

def test_build_huffman_tree():
    """Test Huffman tree construction"""
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16}
    tree_root = build_huffman_tree(freq_dict)
    
    assert tree_root is not None
    assert tree_root.freq == sum(freq_dict.values())
    
    # Test empty dictionary
    assert build_huffman_tree({}) is None

def test_build_huffman_codes():
    """Test Huffman code generation"""
    # Create a simple tree
    root = HuffmanNode(None, 15)
    root.left = HuffmanNode('a', 5)
    root.right = HuffmanNode('b', 10)
    
    codes = build_huffman_codes(root)
    assert codes == {'a': '0', 'b': '1'}
    
    # Test None input
    assert build_huffman_codes(None) == {}

def test_compress_decompress():
    """Test full compression and decompression cycle"""
    test_strings = [
        "hello world",
        "abracadabra",
        "Mississippi",
        "",  # Empty string
        "aaaaaaaaaa"  # Repeated characters
    ]
    
    for test_str in test_strings:
        # Compress
        compressed, tree = compress(test_str)
        
        # Decompress
        decompressed = decompress(compressed, tree)
        
        # Verify
        assert decompressed == test_str, f"Failed for input: {test_str}"

def test_edge_cases():
    """Test edge cases for compression and decompression"""
    # None or empty inputs
    assert compress("")[0] == ""
    assert decompress("", None) == ""
    
    # Single character
    single_char = "x"
    compressed, tree = compress(single_char)
    assert decompress(compressed, tree) == single_char

def test_invalid_inputs():
    """Test handling of invalid inputs"""
    # These should not raise exceptions
    assert compress(None)[0] == ""
    assert decompress("", None) == ""