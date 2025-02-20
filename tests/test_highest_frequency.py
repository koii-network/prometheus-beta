import pytest
from src.highest_frequency import find_highest_frequency_index

def test_single_highest_frequency():
    """Test a list with a clear highest frequency number"""
    assert find_highest_frequency_index([1, 2, 2, 3, 3, 3]) == 3
    
def test_first_occurrence_in_tie():
    """Test that the first occurrence is returned in case of a frequency tie"""
    assert find_highest_frequency_index([1, 2, 2, 1, 3, 3]) == 0
    
def test_all_unique_numbers():
    """Test a list where all numbers appear once"""
    assert find_highest_frequency_index([1, 2, 3, 4, 5]) == 0
    
def test_single_element_list():
    """Test a list with a single element"""
    assert find_highest_frequency_index([42]) == 0
    
def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_highest_frequency_index([])
    
def test_multiple_max_frequency_numbers():
    """Test a scenario with multiple numbers having the same max frequency"""
    assert find_highest_frequency_index([1, 2, 2, 1, 3, 3]) == 0