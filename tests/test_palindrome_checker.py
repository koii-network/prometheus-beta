import pytest
from src.palindrome_checker import is_palindrome

def test_empty_list():
    """Test that an empty list is considered a palindrome."""
    assert is_palindrome([]) == True

def test_single_element_list():
    """Test that a single-element list is a palindrome."""
    assert is_palindrome([42]) == True

def test_palindrome_even_length():
    """Test a palindrome with even number of elements."""
    assert is_palindrome([1, 2, 2, 1]) == True

def test_palindrome_odd_length():
    """Test a palindrome with odd number of elements."""
    assert is_palindrome([1, 2, 3, 2, 1]) == True

def test_non_palindrome():
    """Test a non-palindrome list."""
    assert is_palindrome([1, 2, 3, 4]) == False

def test_negative_numbers_palindrome():
    """Test a palindrome with negative numbers."""
    assert is_palindrome([-1, 0, -1]) == True

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome("not a list")
        is_palindrome(123)
        is_palindrome(None)