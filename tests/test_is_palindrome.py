import pytest
from src.is_palindrome import is_palindrome

def test_palindrome_list_odd_length():
    """Test palindrome with odd number of elements"""
    assert is_palindrome([1, 2, 1]) == True

def test_palindrome_list_even_length():
    """Test palindrome with even number of elements"""
    assert is_palindrome([1, 2, 2, 1]) == True

def test_not_palindrome():
    """Test non-palindrome list"""
    assert is_palindrome([1, 2, 3, 4]) == False

def test_empty_list():
    """Test empty list (considered a palindrome)"""
    assert is_palindrome([]) == True

def test_single_element_list():
    """Test single element list (always a palindrome)"""
    assert is_palindrome([42]) == True

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome("not a list")

def test_large_palindrome_list():
    """Test a larger palindrome list"""
    assert is_palindrome([1, 2, 3, 4, 3, 2, 1]) == True

def test_large_non_palindrome_list():
    """Test a larger non-palindrome list"""
    assert is_palindrome([1, 2, 3, 4, 5, 6, 7]) == False