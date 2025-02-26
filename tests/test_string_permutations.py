import pytest
from src.string_permutations import generate_unique_permutations

def test_generate_unique_permutations_typical_string():
    """Test unique permutations for a string with unique characters."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_with_duplicates():
    """Test unique permutations for a string with duplicate characters."""
    result = generate_unique_permutations('aba')
    expected = ['aba', 'aab', 'baa']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_single_character():
    """Test permutations for a single character string."""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_generate_unique_permutations_empty_string():
    """Test permutations for an empty string."""
    result = generate_unique_permutations('')
    assert result == ['']

def test_generate_unique_permutations_all_same_characters():
    """Test permutations for a string with all same characters."""
    result = generate_unique_permutations('aaa')
    assert result == ['aaa']

def test_result_type_and_uniqueness():
    """Verify the result is a list of unique strings."""
    result = generate_unique_permutations('abcd')
    assert isinstance(result, list)
    assert len(result) == len(set(result))  # Ensure all elements are unique