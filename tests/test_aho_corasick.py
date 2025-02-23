import pytest
from src.aho_corasick import AhoCorasick

def test_basic_matching():
    """Test basic pattern matching"""
    ac = AhoCorasick(["he", "she", "his", "hers"])
    text = "she sells seashells by the seashore"
    matches = ac.find_matches(text)
    
    assert len(matches) == 2
    assert (1, "she") in matches
    assert (19, "he") in matches

def test_overlapping_matches():
    """Test matching overlapping patterns"""
    ac = AhoCorasick(["ab", "abc", "bc"])
    text = "abcdef"
    matches = ac.find_matches(text)
    
    assert len(matches) == 3
    assert (0, "ab") in matches
    assert (0, "abc") in matches
    assert (1, "bc") in matches

def test_multiple_occurrences():
    """Test multiple occurrences of patterns"""
    ac = AhoCorasick(["a", "ab"])
    text = "ababa"
    matches = ac.find_matches(text)
    
    assert len(matches) == 5
    # Check for single character 'a' matches
    assert (0, "a") in matches
    assert (2, "a") in matches
    assert (4, "a") in matches
    # Check for 'ab' matches
    assert (0, "ab") in matches
    assert (2, "ab") in matches

def test_no_matches():
    """Test scenario with no matches"""
    ac = AhoCorasick(["hello", "world"])
    text = "python is awesome"
    matches = ac.find_matches(text)
    
    assert len(matches) == 0

def test_empty_pattern_raises_error():
    """Test that empty pattern list raises ValueError"""
    with pytest.raises(ValueError):
        AhoCorasick([])

def test_non_string_input():
    """Test that non-string input raises TypeError"""
    ac = AhoCorasick(["test"])
    
    with pytest.raises(TypeError):
        ac.find_matches(123)
    with pytest.raises(TypeError):
        ac.find_matches(None)

def test_case_sensitive_matching():
    """Test case-sensitive matching"""
    ac = AhoCorasick(["Hello", "hello"])
    text = "hello HELLO world"
    matches = ac.find_matches(text)
    
    assert len(matches) == 1
    assert (0, "hello") in matches

def test_pattern_as_substring():
    """Test matching patterns that are substrings"""
    ac = AhoCorasick(["a", "aa", "aaa"])
    text = "aaaa"
    matches = ac.find_matches(text)
    
    assert len(matches) == 7  # All possible matches
    expected_matches = [
        (0, "a"), (1, "a"), (2, "a"), (3, "a"),
        (0, "aa"), (1, "aa"), (0, "aaa")
    ]
    for match in expected_matches:
        assert match in matches