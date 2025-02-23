import pytest
from src.rabin_karp import rabin_karp_search

def test_basic_string_matching():
    """Test basic string matching with multiple occurrences"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    result = rabin_karp_search(text, pattern)
    assert result == [10], f"Expected [10], but got {result}"

def test_no_match():
    """Test when pattern is not in the text"""
    text = "Hello, world!"
    pattern = "python"
    result = rabin_karp_search(text, pattern)
    assert result == [], f"Expected [], but got {result}"

def test_single_match():
    """Test when pattern appears only once"""
    text = "hello world hello python"
    pattern = "python"
    result = rabin_karp_search(text, pattern)
    assert result == [18], f"Expected [18], but got {result}"

def test_multiple_matches():
    """Test with multiple matches of the pattern"""
    text = "AAAAAAA"
    pattern = "AA"
    result = rabin_karp_search(text, pattern)
    assert result == [0, 1, 2, 3, 4, 5], f"Expected [0, 1, 2, 3, 4, 5], but got {result}"

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "short"
    pattern = "longer pattern"
    result = rabin_karp_search(text, pattern)
    assert result == [], f"Expected [], but got {result}"

def test_empty_pattern():
    """Test when pattern is empty"""
    with pytest.raises(ValueError, match="Pattern cannot be empty"):
        rabin_karp_search("text", "")

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Both text and pattern must be strings"):
        rabin_karp_search(123, "pattern")
    
    with pytest.raises(TypeError, match="Both text and pattern must be strings"):
        rabin_karp_search("text", 456)

def test_case_sensitive():
    """Test that search is case-sensitive"""
    text = "Hello World hello"
    pattern = "hello"
    result = rabin_karp_search(text, pattern)
    assert result == [12], f"Expected [12], but got {result}"

def test_overlapping_matches():
    """Test handling of overlapping matches"""
    text = "AAAAA"
    pattern = "AA"
    result = rabin_karp_search(text, pattern)
    assert result == [0, 1, 2, 3], f"Expected [0, 1, 2, 3], but got {result}"