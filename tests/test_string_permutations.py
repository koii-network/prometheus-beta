import pytest
from src.string_permutations import generate_unique_permutations

def test_generate_unique_permutations_basic():
    """Test basic string permutations"""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_with_duplicates():
    """Test string with duplicate characters"""
    result = generate_unique_permutations('abb')
    expected = ['abb', 'bab', 'bba']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_single_char():
    """Test single character string"""
    result = generate_unique_permutations('a')
    expected = ['a']
    assert result == expected

def test_generate_unique_permutations_empty_string():
    """Test empty string"""
    result = generate_unique_permutations('')
    expected = ['']
    assert result == expected

def test_generate_unique_permutations_longer_string():
    """Test longer string with more permutations"""
    result = generate_unique_permutations('abcd')
    assert len(result) == 24  # 4! = 24 unique permutations

def test_generate_unique_permutations_type_error():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError):
        generate_unique_permutations(123)