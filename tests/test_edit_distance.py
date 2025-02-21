import pytest
from src.edit_distance import compute_edit_distance

def test_edit_distance_identical_strings():
    assert compute_edit_distance("hello", "hello") == 0

def test_edit_distance_different_strings():
    assert compute_edit_distance("kitten", "sitting") == 3

def test_edit_distance_empty_strings():
    assert compute_edit_distance("", "") == 0

def test_edit_distance_one_empty_string():
    assert compute_edit_distance("", "hello") == 5
    assert compute_edit_distance("hello", "") == 5

def test_edit_distance_different_lengths():
    assert compute_edit_distance("abc", "abcd") == 1
    assert compute_edit_distance("abcd", "abc") == 1

def test_edit_distance_case_sensitive():
    assert compute_edit_distance("Hello", "hello") == 1

def test_edit_distance_error_handling():
    with pytest.raises(ValueError):
        compute_edit_distance(None, "test")
    with pytest.raises(ValueError):
        compute_edit_distance("test", None)
    with pytest.raises(ValueError):
        compute_edit_distance(None, None)