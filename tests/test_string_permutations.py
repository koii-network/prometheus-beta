import pytest
from src.string_permutations import generate_unique_permutations

def test_generate_unique_permutations_normal_string():
    """Test generating permutations for a normal string."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_empty_string():
    """Test generating permutations for an empty string."""
    result = generate_unique_permutations('')
    assert result == []

def test_generate_unique_permutations_single_char():
    """Test generating permutations for a single character."""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_generate_unique_permutations_duplicate_chars():
    """Test generating unique permutations with duplicate characters."""
    result = generate_unique_permutations('abb')
    expected = ['abb', 'bab', 'bba']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_return_type():
    """Test that the function returns a list."""
    result = generate_unique_permutations('abc')
    assert isinstance(result, list)

def test_generate_unique_permutations_no_duplicates():
    """Test that the returned permutations are unique."""
    result = generate_unique_permutations('aab')
    assert len(result) == len(set(result))