import pytest
from src.levenshtein_distance import compute_levenshtein_distance

def test_levenshtein_distance_same_strings():
    """Test distance between identical strings is 0"""
    assert compute_levenshtein_distance("hello", "hello") == 0

def test_levenshtein_distance_empty_strings():
    """Test distance between empty strings"""
    assert compute_levenshtein_distance("", "") == 0

def test_levenshtein_distance_one_empty_string():
    """Test distance when one string is empty"""
    assert compute_levenshtein_distance("hello", "") == 5
    assert compute_levenshtein_distance("", "world") == 5

def test_levenshtein_distance_different_strings():
    """Test distance between different strings"""
    assert compute_levenshtein_distance("kitten", "sitting") == 3
    assert compute_levenshtein_distance("saturday", "sunday") == 3

def test_levenshtein_distance_case_sensitive():
    """Test that function is case-sensitive"""
    assert compute_levenshtein_distance("Hello", "hello") == 1

def test_levenshtein_distance_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compute_levenshtein_distance(123, "hello")
    with pytest.raises(TypeError):
        compute_levenshtein_distance("hello", ["world"])