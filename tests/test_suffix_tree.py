import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_basic_search():
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Test existing patterns
    assert suffix_tree.search("banana") == True
    assert suffix_tree.search("anana") == True
    assert suffix_tree.search("nana") == True
    assert suffix_tree.search("ana") == True
    assert suffix_tree.search("na") == True
    assert suffix_tree.search("a") == True
    
    # Test non-existing patterns
    assert suffix_tree.search("bananas") == False
    assert suffix_tree.search("banan") == False
    assert suffix_tree.search("x") == False

def test_suffix_tree_edge_cases():
    # Empty string
    suffix_tree = SuffixTree("")
    assert suffix_tree.search("") == False
    assert suffix_tree.search("a") == False

    # Single character
    suffix_tree = SuffixTree("a")
    assert suffix_tree.search("a") == True
    assert suffix_tree.search("b") == False

def test_suffix_tree_complex_patterns():
    text = "mississippi"
    suffix_tree = SuffixTree(text)
    
    # Complex pattern checks
    assert suffix_tree.search("mississippi") == True
    assert suffix_tree.search("issippi") == True
    assert suffix_tree.search("sippi") == True
    assert suffix_tree.search("ippi") == True
    
    # Partial matches
    assert suffix_tree.search("miss") == True
    assert suffix_tree.search("sip") == True
    
    # Non-existent patterns
    assert suffix_tree.search("missi ") == False
    assert suffix_tree.search("misisippi") == False

def test_suffix_tree_case_sensitivity():
    text = "Hello World"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("Hello") == True
    assert suffix_tree.search("hello") == False  # Case sensitive
    assert suffix_tree.search("World") == True
    assert suffix_tree.search("world") == False  # Case sensitive

def test_suffix_tree_special_characters():
    text = "hello@world#123"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("hello@world#123") == True
    assert suffix_tree.search("@world") == True
    assert suffix_tree.search("#123") == True
    assert suffix_tree.search("hello@") == False