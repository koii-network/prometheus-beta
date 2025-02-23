import pytest
from src.kmp_matcher import kmp_search, compute_lps

def test_compute_lps_basic():
    """Test basic LPS computation"""
    assert compute_lps("AAAA") == [0, 1, 2, 3]
    assert compute_lps("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

def test_compute_lps_edge_cases():
    """Test edge cases for LPS computation"""
    assert compute_lps("") == []
    assert compute_lps("A") == [0]

def test_compute_lps_invalid_input():
    """Test invalid input for LPS computation"""
    with pytest.raises(TypeError):
        compute_lps(123)
    with pytest.raises(TypeError):
        compute_lps(None)

def test_kmp_search_basic():
    """Test basic string matching"""
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [9]
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("hello world", "world") == [6]

def test_kmp_search_multiple_matches():
    """Test scenarios with multiple matches"""
    assert kmp_search("AAAAAAAA", "AAA") == [0, 1, 2, 3, 4, 5]
    assert kmp_search("ABABABAB", "ABAB") == [0, 2, 4]

def test_kmp_search_no_matches():
    """Test scenarios with no matches"""
    assert kmp_search("hello world", "python") == []
    assert kmp_search("hello", "world") == []

def test_kmp_search_edge_cases():
    """Test edge cases for KMP search"""
    # Empty text
    assert kmp_search("", "pattern") == []
    
    # Empty pattern (should raise ValueError)
    with pytest.raises(ValueError):
        kmp_search("text", "")
    
    # Pattern longer than text
    assert kmp_search("short", "longer pattern") == []

def test_kmp_search_invalid_input():
    """Test invalid input for KMP search"""
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    with pytest.raises(TypeError):
        kmp_search("text", 456)
    with pytest.raises(TypeError):
        kmp_search(None, None)