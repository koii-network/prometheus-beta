import pytest
from src.palindrome_check import is_palindrome

def test_empty_list_is_palindrome():
    assert is_palindrome([]) == True

def test_single_element_list_is_palindrome():
    assert is_palindrome([5]) == True

def test_simple_palindrome_list():
    assert is_palindrome([1, 2, 1]) == True
    assert is_palindrome([1, 2, 2, 1]) == True

def test_non_palindrome_list():
    assert is_palindrome([1, 2, 3]) == False
    assert is_palindrome([1, 2, 4, 1]) == False

def test_large_palindrome_list():
    assert is_palindrome([1, 2, 3, 3, 2, 1]) == True

def test_non_list_input_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome("not a list")
    
    with pytest.raises(TypeError):
        is_palindrome(123)
    
    with pytest.raises(TypeError):
        is_palindrome(None)