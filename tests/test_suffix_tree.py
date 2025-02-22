import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_basic_search():
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Test existing patterns
    assert suffix_tree.search("banana") == [0]
    assert suffix_tree.search("ana") == [1, 3]
    assert suffix_tree.search("na") == [2, 4]
    
    # Test non-existing patterns
    assert suffix_tree.search("ananas") == []
    assert suffix_tree.search("apple") == []

def test_suffix_tree_empty_string():
    suffix_tree = SuffixTree("")
    
    assert suffix_tree.search("test") == []
    assert suffix_tree.search("") == []

def test_suffix_tree_long_text():
    text = "abracadabra" * 5
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("abracadabra") == list(range(0, len(text), 11))
    assert len(suffix_tree.search("bracadabr")) > 0

def test_suffix_tree_repeated_substrings():
    text = "mississippi"
    suffix_tree = SuffixTree(text)
    
    assert len(suffix_tree.search("iss")) == 2
    assert suffix_tree.search("ssi") == [2, 3]

def test_suffix_tree_case_sensitivity():
    text = "HelloWorld"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("hello") == []
    assert suffix_tree.search("Hello") == [0]
    assert suffix_tree.search("World") == [5]

def test_suffix_tree_unicode_text():
    text = "こんにちは世界"
    suffix_tree = SuffixTree(text)
    
    assert len(suffix_tree.search("ちは")) > 0
    assert suffix_tree.search("世界") == [4]