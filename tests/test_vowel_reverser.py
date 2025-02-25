import pytest
from src.vowel_reverser import reverse_vowels_in_substring

def test_reverse_vowels_in_substring_basic():
    """Test basic substring vowel reversal."""
    assert reverse_vowels_in_substring("hello world", 0, 5) == "hollo werld"

def test_reverse_vowels_in_substring_full_string():
    """Test reversing vowels in the entire string."""
    assert reverse_vowels_in_substring("hello world", 0, 11) == "hollo werld"

def test_reverse_vowels_in_substring_no_vowels():
    """Test a substring with no vowels."""
    assert reverse_vowels_in_substring("hello world", 6, 11) == "hello world"

def test_reverse_vowels_in_substring_mixed_case():
    """Test reversing vowels with mixed case."""
    assert reverse_vowels_in_substring("HeLLo WoRLd", 0, 5) == "HoLLe WoRLd"

def test_reverse_vowels_in_substring_only_vowels():
    """Test a substring containing only vowels."""
    assert reverse_vowels_in_substring("aeiou", 0, 5) == "uoiea"

def test_reverse_vowels_in_substring_empty_string():
    """Test an empty string."""
    assert reverse_vowels_in_substring("", 0, 0) == ""

def test_reverse_vowels_in_substring_start_eq_end():
    """Test when start and end indices are the same."""
    assert reverse_vowels_in_substring("hello world", 0, 0) == "hello world"

def test_reverse_vowels_in_substring_out_of_bounds():
    """Test that out-of-bounds indices raise ValueError."""
    with pytest.raises(ValueError, match="Start or end indices are out of bounds."):
        reverse_vowels_in_substring("hello", -1, 5)
    with pytest.raises(ValueError, match="Start or end indices are out of bounds."):
        reverse_vowels_in_substring("hello", 0, 6)

def test_reverse_vowels_in_substring_invalid_indices():
    """Test that invalid index order raises ValueError."""
    with pytest.raises(ValueError, match="Start index must be less than or equal to end index."):
        reverse_vowels_in_substring("hello", 3, 2)