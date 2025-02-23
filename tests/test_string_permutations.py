import pytest
from src.string_permutations import generate_unique_permutations

def test_basic_permutations():
    """Test basic string permutations."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_single_character():
    """Test permutations of a single character."""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_repeated_characters():
    """Test permutations with repeated characters."""
    result = generate_unique_permutations('abb')
    expected = ['abb', 'bab', 'bba']
    assert sorted(result) == sorted(expected)

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        generate_unique_permutations('')

def test_non_string_input_raises_error():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(123)

def test_numeric_string_permutations():
    """Test permutations of a numeric string."""
    result = generate_unique_permutations('123')
    expected = ['123', '132', '213', '231', '312', '321']
    assert sorted(result) == sorted(expected)

def test_mixed_case_string():
    """Test permutations with mixed case characters."""
    result = generate_unique_permutations('AbC')
    expected = ['AbC', 'ACb', 'bAC', 'bCA', 'CAb', 'CbA']
    assert sorted(result) == sorted(expected)