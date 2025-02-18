import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_search():
    # Test basic search functionality
    text = "bananabanaba"
    suffix_tree = SuffixTree(text)
    
    # Test patterns that exist
    assert suffix_tree.search("banana") == True
    assert suffix_tree.search("ana") == True
    assert suffix_tree.search("anaba") == True
    
    # Test patterns that do not exist
    assert suffix_tree.search("orange") == False
    assert suffix_tree.search("bananaa") == False
    assert suffix_tree.search("") == False

def test_find_all_occurrences():
    # Test finding all occurrences of a pattern
    text = "bananabanaba"
    suffix_tree = SuffixTree(text)
    
    # Test different patterns
    assert suffix_tree.find_all_occurrences("ana") == [3, 1]
    assert suffix_tree.find_all_occurrences("banana") == [0]
    assert suffix_tree.find_all_occurrences("anaba") == [6]
    
    # Test non-existent patterns
    assert suffix_tree.find_all_occurrences("orange") == []
    assert suffix_tree.find_all_occurrences("") == []

def test_edge_cases():
    # Test with empty string
    suffix_tree = SuffixTree("")
    assert suffix_tree.search("anything") == False
    assert suffix_tree.find_all_occurrences("anything") == []

    # Test with single character
    suffix_tree = SuffixTree("a")
    assert suffix_tree.search("a") == True
    assert suffix_tree.search("b") == False
    assert suffix_tree.find_all_occurrences("a") == [0]