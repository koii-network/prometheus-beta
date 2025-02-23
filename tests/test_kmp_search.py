import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_lps_array_basic():
    """Test basic LPS array computation"""
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("ABABC") == [0, 0, 1, 2, 0]

def test_kmp_search_basic():
    """Test basic string matching scenarios"""
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("hello world", "world") == [6]
    assert kmp_search("mississippi", "issip") == [4]

def test_kmp_search_multiple_matches():
    """Test scenarios with multiple pattern matches"""
    assert kmp_search("AAAAAAAA", "AAA") == [0, 1, 2, 3, 4, 5]
    assert kmp_search("ABABABAB", "ABAB") == [0, 2, 4]

def test_kmp_search_no_matches():
    """Test scenarios with no pattern matches"""
    assert kmp_search("hello world", "python") == []
    assert kmp_search("abc", "def") == []

def test_kmp_search_edge_cases():
    """Test edge cases in string matching"""
    # Empty text
    assert kmp_search("", "pattern") == []
    
    # Empty pattern (should raise ValueError)
    with pytest.raises(ValueError):
        kmp_search("text", "")
    
def test_kmp_search_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Non-string inputs
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        kmp_search("text", 456)

def test_kmp_search_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    assert kmp_search("abc", "abcdef") == []

def test_kmp_search_case_sensitive():
    """Test case sensitivity of matching"""
    assert kmp_search("Hello World", "world") == []
    assert kmp_search("Hello World", "World") == [6]