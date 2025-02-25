import pytest
from src.palindrome_pairs import find_palindrome_pair_indices

def test_basic_palindrome_pairs():
    """Test basic palindrome pair detection."""
    words = ['bat', 'tab', 'cat']
    assert set(find_palindrome_pair_indices(words)) == {(0, 1), (1, 0)}

def test_multiple_palindrome_pairs():
    """Test finding multiple palindrome pairs."""
    words = ['race', 'care', 'deer', 'reed']
    assert set(find_palindrome_pair_indices(words)) == {(2, 3), (3, 2)}

def test_no_palindrome_pairs():
    """Test when no palindrome pairs exist."""
    words = ['hello', 'world', 'python']
    assert find_palindrome_pair_indices(words) == []

def test_empty_list():
    """Test with an empty list."""
    assert find_palindrome_pair_indices([]) == []

def test_single_element_list():
    """Test with a list containing only one element."""
    words = ['single']
    assert find_palindrome_pair_indices(words) == []

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_palindrome_pair_indices("not a list")

def test_invalid_list_elements():
    """Test that ValueError is raised for non-string list elements."""
    with pytest.raises(ValueError, match="All elements must be strings"):
        find_palindrome_pair_indices(['valid', 42, 'invalid'])

def test_case_sensitive():
    """Test that the function is case-sensitive."""
    words = ['Race', 'care']
    assert find_palindrome_pair_indices(words) == []