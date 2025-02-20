import pytest
from src.palindrome import is_palindrome

def test_empty_list_is_palindrome():
    """Test that an empty list is considered a palindrome"""
    assert is_palindrome([]) == True

def test_single_element_list_is_palindrome():
    """Test that a single-element list is a palindrome"""
    assert is_palindrome([5]) == True

def test_odd_length_palindrome():
    """Test a palindrome with odd number of elements"""
    assert is_palindrome([1, 2, 1]) == True

def test_even_length_palindrome():
    """Test a palindrome with even number of elements"""
    assert is_palindrome([1, 2, 2, 1]) == True

def test_non_palindrome():
    """Test a list that is not a palindrome"""
    assert is_palindrome([1, 2, 3]) == False

def test_longer_palindrome():
    """Test a longer palindrome"""
    assert is_palindrome([1, 2, 3, 3, 2, 1]) == True

def test_not_a_palindrome_with_same_length():
    """Test a non-palindrome with the same length as a palindrome"""
    assert is_palindrome([1, 2, 3, 4, 5]) == False

def test_input_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome(None)