import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_basic_substring_search():
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Test basic substring searches
    assert suffix_tree.find_substring("ana") == [1, 3]
    assert suffix_tree.find_substring("banana") == [0]
    assert sorted(suffix_tree.find_substring("an")) == [1, 3]

def test_suffix_tree_edge_cases():
    # Empty string
    suffix_tree = SuffixTree("")
    assert suffix_tree.find_substring("test") == []

    # Single character string
    suffix_tree = SuffixTree("a")
    assert suffix_tree.find_substring("a") == [0]
    assert suffix_tree.find_substring("b") == []

def test_suffix_tree_multiple_occurrences():
    text = "mississippi"
    suffix_tree = SuffixTree(text)
    
    # Test multiple occurrence substrings
    assert sorted(suffix_tree.find_substring("iss")) == [1, 4]
    assert suffix_tree.find_substring("ssi") == [2, 5]

def test_suffix_tree_non_existent_substring():
    text = "hello world"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.find_substring("python") == []
    assert suffix_tree.find_substring("xyz") == []

def test_suffix_tree_unicode_support():
    text = "こんにちは世界"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.find_substring("にち") != []
    assert suffix_tree.find_substring("世界") != []

def test_suffix_tree_long_text():
    text = "a" * 1000
    suffix_tree = SuffixTree(text)
    
    assert len(suffix_tree.find_substring("a")) == 1000
    assert suffix_tree.find_substring("b") == []

def test_suffix_tree_case_sensitivity():
    text = "HelloWorld"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.find_substring("hello") == []
    assert suffix_tree.find_substring("Hello") != []