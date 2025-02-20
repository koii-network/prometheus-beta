import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1, 1]
    expected = [1]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    with pytest.raises(TypeError):
        remove_duplicates(123)
    with pytest.raises(TypeError):
        remove_duplicates(None)

def test_remove_duplicates_order_preservation():
    """Test order preservation of unique elements"""
    input_list = [5, 2, 8, 2, 1, 5, 3, 9, 4, 8, 7]
    expected = [5, 2, 8, 1, 3, 9, 4, 7]
    assert remove_duplicates(input_list) == expected