import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_initialization():
    """Test basic initialization of Suffix Tree"""
    text = "banana"
    tree = SuffixTree(text)
    assert tree.text == "banana$"
    assert tree.root is not None

def test_empty_string_initialization():
    """Test initialization with an empty string raises ValueError"""
    with pytest.raises(ValueError):
        SuffixTree("")

def test_simple_search():
    """Test basic pattern searching in the suffix tree"""
    text = "banana"
    tree = SuffixTree(text)
    
    # Positive searches
    assert tree.search("banana") == True
    assert tree.search("ban") == True
    assert tree.search("ana") == True
    
    # Negative searches
    assert tree.search("ananas") == False
    assert tree.search("bananaa") == False
    assert tree.search("") == False

def test_find_all_occurrences():
    """Test finding all occurrences of a pattern"""
    text = "bananabanana"
    tree = SuffixTree(text)
    
    # Find occurrences of 'banana'
    occurrences = tree.find_all_occurrences("banana")
    assert set(occurrences) == {0, 6}
    
    # Find occurrences of 'ana'
    occurrences = tree.find_all_occurrences("ana")
    assert set(occurrences) == {1, 3, 7, 9}
    
    # Non-existent pattern
    occurrences = tree.find_all_occurrences("xyz")
    assert occurrences == []

def test_edge_cases():
    """Test various edge cases"""
    # Single character text
    tree = SuffixTree("a")
    assert tree.search("a") == True
    assert tree.search("b") == False
    
    # Repeated characters
    tree = SuffixTree("aaaaa")
    assert tree.search("aaa") == True
    assert tree.find_all_occurrences("aa") == [0, 1, 2, 3]