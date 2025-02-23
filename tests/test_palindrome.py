import pytest
from src.palindrome import is_palindrome

def test_is_palindrome_empty_list():
    """Test that an empty list is considered a palindrome."""
    assert is_palindrome([]) == True

def test_is_palindrome_single_element():
    """Test that a single-element list is a palindrome."""
    assert is_palindrome([42]) == True

def test_is_palindrome_true_cases():
    """Test various true palindrome cases."""
    assert is_palindrome([1, 2, 1]) == True
    assert is_palindrome([1, 2, 2, 1]) == True
    assert is_palindrome([5, 4, 3, 4, 5]) == True

def test_is_palindrome_false_cases():
    """Test various false (non-palindrome) cases."""
    assert is_palindrome([1, 2, 3]) == False
    assert is_palindrome([1, 2, 3, 4]) == False
    assert is_palindrome([1, 2, 1, 3]) == False

def test_is_palindrome_type_error():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        is_palindrome(None)