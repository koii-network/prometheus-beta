import pytest
from src.string_case_switcher import switch_cases

def test_basic_case_switching():
    """Test basic case switching functionality."""
    assert switch_cases("HelloWorld", "abc") == "hELLOwORLd"

def test_different_length_strings():
    """Test case switching with strings of different lengths."""
    assert switch_cases("Python", "xyx") == "pYTHON"

def test_empty_strings():
    """Test behavior with empty strings."""
    assert switch_cases("", "test") == ""
    assert switch_cases("Hello", "") == ""

def test_non_alphabetic_characters():
    """Test handling of non-alphabetic characters."""
    assert switch_cases("Hello123World!", "abc") == "hELLO123wORLD!"

def test_all_uppercase():
    """Test switching case for all uppercase string."""
    assert switch_cases("HELLO", "xyz") == "hello"

def test_all_lowercase():
    """Test switching case for all lowercase string."""
    assert switch_cases("hello", "abc") == "HELLO"

def test_mixed_case():
    """Test switching case for mixed case string."""
    assert switch_cases("MixEd CaSe", "pattern") == "mIXeD cAsE"

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        switch_cases(123, "test")
    
    with pytest.raises(TypeError):
        switch_cases("test", None)

def test_unicode_characters():
    """Test handling of unicode characters."""
    assert switch_cases("Héllö", "xyz") == "hÉLLÖ"