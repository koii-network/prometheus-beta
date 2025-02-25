import pytest
import src.huffman_coding as hc

def test_build_frequency_dict():
    # Test normal case
    freq_dict = hc.build_frequency_dict("hello world")
    assert freq_dict == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    
    # Test empty string
    assert hc.build_frequency_dict("") == {}

def test_build_huffman_tree():
    # Test with sample frequency dict
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    tree = hc.build_huffman_tree(freq_dict)
    
    # Verify tree properties
    assert tree is not None
    assert tree.char is None  # Root should be an internal node
    assert tree.freq == sum(freq_dict.values())

    # Test empty dict
    assert hc.build_huffman_tree({}) is None

def test_build_huffman_codes():
    # Create a sample tree
    root = hc.HuffmanNode(None, 100)
    root.left = hc.HuffmanNode('a', 45)
    root.right = hc.HuffmanNode(None, 55)
    root.right.left = hc.HuffmanNode('b', 25)
    root.right.right = hc.HuffmanNode('c', 30)
    
    # Get codes
    codes = hc.build_huffman_codes(root)
    
    # Verify codes
    assert codes == {'a': '0', 'b': '10', 'c': '11'}

    # Test empty tree
    assert hc.build_huffman_codes(None) == {}

def test_compress_decompress():
    # Test various scenarios
    test_cases = [
        "hello world",
        "abracadabra",
        "aaabbbcccddd",
        "",
        "x"
    ]
    
    for original in test_cases:
        # Compress
        compressed, tree = hc.compress(original)
        
        # Decompress
        decompressed = hc.decompress(compressed, tree)
        
        # Verify
        assert decompressed == original, f"Failed for input: {original}"

def test_edge_cases():
    # Test compression and decompression with empty input
    compressed, tree = hc.compress("")
    assert compressed == ""
    assert tree is None
    
    decompressed = hc.decompress("", None)
    assert decompressed == ""

def test_error_handling():
    # Ensure no unhandled exceptions for various inputs
    with pytest.raises(TypeError):
        hc.compress(None)
    
    with pytest.raises(TypeError):
        hc.decompress(None, None)