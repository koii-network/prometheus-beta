import pytest
from src.array_matching import count_matching_elements

def test_basic_matching():
    """Test basic matching scenario"""
    assert count_matching_elements([1, 2, 3], [3, 4, 5]) == 1

def test_multiple_matches():
    """Test scenario with multiple matches"""
    assert count_matching_elements([1, 2, 3, 4], [3, 4, 5, 6]) == 2

def test_no_matches():
    """Test scenario with no matches"""
    assert count_matching_elements([1, 2], [3, 4]) == 0

def test_empty_arrays():
    """Test scenario with empty arrays"""
    assert count_matching_elements([], [1, 2, 3]) == 0
    assert count_matching_elements([1, 2, 3], []) == 0

def test_repeated_elements():
    """Test scenario with repeated elements"""
    assert count_matching_elements([1, 1, 2, 2], [2, 3]) == 2

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        count_matching_elements(123, [1, 2, 3])
    
    with pytest.raises(TypeError):
        count_matching_elements([1, 2, 3], "not a list")

def test_different_types_in_arrays():
    """Test matching with different types of elements"""
    assert count_matching_elements([1, '2', 3], [3, '2', 5]) == 2