import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_arr = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_arr) == expected

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates"""
    input_arr = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_arr) == input_arr

def test_remove_duplicates_all_duplicates():
    """Test with a list of all duplicates"""
    input_arr = [1, 1, 1, 1]
    assert remove_duplicates(input_arr) == [1]

def test_remove_duplicates_invalid_input():
    """Test with invalid input types"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    
    with pytest.raises(TypeError):
        remove_duplicates(123)
    
    with pytest.raises(TypeError):
        remove_duplicates(None)

def test_remove_duplicates_preserve_order():
    """Test that the first occurrence of each number is preserved"""
    input_arr = [3, 1, 2, 3, 4, 1, 2, 5]
    expected = [3, 1, 2, 4, 5]
    assert remove_duplicates(input_arr) == expected