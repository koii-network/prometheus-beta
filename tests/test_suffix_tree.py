import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_basic_search():
    # Test basic pattern search
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("ban") == True
    assert suffix_tree.search("ana") == True
    assert suffix_tree.search("nana") == True
    assert suffix_tree.search("apple") == False

def test_suffix_tree_find_occurrences():
    # Test finding all occurrences of a pattern
    text = "bananabanana"
    suffix_tree = SuffixTree(text)
    
    occurrences = suffix_tree.find_all_occurrences("banana")
    assert len(occurrences) == 2
    assert 0 in occurrences
    assert 6 in occurrences

def test_suffix_tree_empty_text():
    # Test with an empty text
    suffix_tree = SuffixTree("")
    
    assert suffix_tree.search("") == True
    assert suffix_tree.find_all_occurrences("test") == []

def test_suffix_tree_single_character():
    # Test with a single character text
    text = "a"
    suffix_tree = SuffixTree(text)
    
    assert suffix_tree.search("a") == True
    assert suffix_tree.search("b") == False
    
    occurrences = suffix_tree.find_all_occurrences("a")
    assert len(occurrences) == 1
    assert occurrences[0] == 0

def test_suffix_tree_repeated_pattern():
    # Test text with repeated patterns
    text = "aaaaa"
    suffix_tree = SuffixTree(text)
    
    occurrences = suffix_tree.find_all_occurrences("aa")
    assert len(occurrences) == 4
    assert occurrences == [0, 1, 2, 3]