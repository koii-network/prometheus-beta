import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_initialization():
    """Test initializing a suffix tree with a valid string."""
    text = "banana"
    tree = SuffixTree(text)
    assert tree.text == "banana$"
    assert isinstance(tree.root, dict)

def test_suffix_tree_invalid_initialization():
    """Test initializing a suffix tree with invalid inputs."""
    with pytest.raises(ValueError):
        SuffixTree("")
    with pytest.raises(ValueError):
        SuffixTree(None)

def test_suffix_tree_search_basic():
    """Test basic substring search functionality."""
    text = "banana"
    tree = SuffixTree(text)
    
    # Test exact matches
    assert tree.search("banana") == [0]
    assert tree.search("ana") == [1, 3]
    assert tree.search("na") == [2, 4]

def test_suffix_tree_search_complex():
    """Test more complex search scenarios."""
    text = "mississippi"
    tree = SuffixTree(text)
    
    # Multiple occurrences
    assert tree.search("iss") == [1, 4]
    assert tree.search("ssi") == [2, 5]
    
    # Non-existent patterns
    assert tree.search("xyz") == []

def test_suffix_tree_search_edge_cases():
    """Test edge cases in search functionality."""
    text = "abcdefg"
    tree = SuffixTree(text)
    
    # Single character search
    assert tree.search("a") == [0]
    assert tree.search("g") == [6]
    
    # Entire string search
    assert tree.search("abcdefg") == [0]

def test_suffix_tree_search_invalid_input():
    """Test search with invalid inputs."""
    text = "hello"
    tree = SuffixTree(text)
    
    with pytest.raises(ValueError):
        tree.search("")
    with pytest.raises(ValueError):
        tree.search(None)

def test_suffix_tree_long_text():
    """Test suffix tree with a longer text."""
    text = "abracadabra" * 10  # Repeating pattern
    tree = SuffixTree(text)
    
    # Multiple occurrences in a repeated text
    assert len(tree.search("abracadabra")) > 1