import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_initialization():
    """Test basic initialization of Suffix Tree"""
    text = "banana"
    suffix_tree = SuffixTree(text)
    assert suffix_tree.text == "banana$"
    assert suffix_tree.root is not None

def test_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a string"):
        SuffixTree(123)
    
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        SuffixTree("")

def test_simple_search():
    """Test basic pattern searching in the suffix tree"""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Test exact substring matches
    assert suffix_tree.search("ana") == [1, 3]
    assert suffix_tree.search("banana") == [0]
    assert suffix_tree.search("an") == [1, 3]

def test_no_match_search():
    """Test searching for patterns that don't exist"""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("x") == []
    assert suffix_tree.search("bananax") == []

def test_search_edge_cases():
    """Test edge cases in pattern searching"""
    text = "mississippi"
    suffix_tree = SuffixTree(text)
    
    # Single character searches
    assert "i" in suffix_tree.search("i")
    assert 1 in suffix_tree.search("i")
    assert 4 in suffix_tree.search("i")
    
    # Full string and overlapping patterns
    assert suffix_tree.search("iss") == [1, 4]

def test_search_invalid_input():
    """Test error handling for invalid search inputs"""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    with pytest.raises(ValueError, match="Pattern must be a string"):
        suffix_tree.search(123)
    
    with pytest.raises(ValueError, match="Pattern cannot be empty"):
        suffix_tree.search("")

def test_long_text_search():
    """Test suffix tree with a longer text"""
    text = "abracadabra"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("abra") == [0, 7]
    assert suffix_tree.search("cadabra") == [4]
    assert suffix_tree.search("z") == []

def test_case_sensitivity():
    """Test case sensitivity of suffix tree"""
    text = "Hello World"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("hello") == []
    assert suffix_tree.search("Hello") == [0]
    assert suffix_tree.search("World") == [6]