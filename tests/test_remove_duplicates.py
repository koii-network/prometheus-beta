import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    assert remove_duplicates(input_list) == [1, 2, 3, 4, 5]

def test_remove_duplicates_order_preservation():
    """Ensure original order is maintained"""
    input_list = [5, 2, 8, 2, 5, 3, 1, 8]
    assert remove_duplicates(input_list) == [5, 2, 8, 3, 1]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_empty_list():
    """Test empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_invalid_input_not_list():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_invalid_input_non_integers():
    """Test list with non-integer elements raises TypeError"""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        remove_duplicates([1, 2, "3", 4])

def test_remove_duplicates_large_unique_set():
    """Test list with more than 10 unique integers"""
    input_list = list(range(15)) + list(range(5))
    expected = list(range(15))
    assert remove_duplicates(input_list) == expected