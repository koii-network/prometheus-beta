import pytest
from src.is_palindrome import is_palindrome

def test_is_palindrome_empty_list():
    """Test that an empty list is considered a palindrome."""
    assert is_palindrome([]) == True

def test_is_palindrome_single_element():
    """Test that a list with a single element is a palindrome."""
    assert is_palindrome([42]) == True

def test_is_palindrome_true_even_length():
    """Test a palindrome list with even number of elements."""
    assert is_palindrome([1, 2, 2, 1]) == True

def test_is_palindrome_true_odd_length():
    """Test a palindrome list with odd number of elements."""
    assert is_palindrome([1, 2, 3, 2, 1]) == True

def test_is_palindrome_false():
    """Test a non-palindrome list."""
    assert is_palindrome([1, 2, 3, 4]) == False

def test_is_palindrome_negative_numbers():
    """Test palindrome with negative numbers."""
    assert is_palindrome([-1, 0, -1]) == True

def test_is_palindrome_type_error():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError):
        is_palindrome("not a list")
        is_palindrome(123)
        is_palindrome(None)