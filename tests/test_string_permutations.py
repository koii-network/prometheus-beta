import pytest
from src.string_permutations import generate_unique_permutations

def test_basic_permutations():
    """Test basic string permutations"""
    assert set(generate_unique_permutations('abc')) == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

def test_permutations_with_duplicates():
    """Test permutations with duplicate characters"""
    assert set(generate_unique_permutations('aab')) == set(['aab', 'aba', 'baa'])

def test_single_character():
    """Test permutations of a single character"""
    assert generate_unique_permutations('a') == ['a']

def test_empty_string():
    """Test permutations of an empty string"""
    assert generate_unique_permutations('') == ['']

def test_longer_string():
    """Test permutations of a longer string"""
    result = generate_unique_permutations('wxyz')
    assert len(result) == 24  # 4! = 24 permutations
    assert set(result) == set(''.join(p) for p in __import__('itertools').permutations('wxyz'))

def test_sorted_output():
    """Verify that output is sorted"""
    result = generate_unique_permutations('cba')
    assert result == sorted(result)

def test_input_types():
    """Ensure the function handles different input types"""
    with pytest.raises(TypeError):
        generate_unique_permutations(123)
    with pytest.raises(TypeError):
        generate_unique_permutations(None)