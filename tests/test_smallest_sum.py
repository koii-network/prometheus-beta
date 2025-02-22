import pytest
from src.smallest_sum import find_smallest_sum

def test_find_smallest_sum_basic():
    """Test basic functionality with positive integers"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_smallest_sum(list1, list2) == 32  # 1*6 + 2*5 + 3*4 = 6 + 10 + 16 = 32

def test_find_smallest_sum_negative_numbers():
    """Test with negative numbers"""
    list1 = [-1, -2, -3]
    list2 = [1, 2, 3]
    assert find_smallest_sum(list1, list2) == -14  # -1*3 + -2*2 + -3*1 = -3 + -4 + -7 = -14

def test_find_smallest_sum_zero():
    """Test with zero values"""
    list1 = [0, 0, 0]
    list2 = [1, 2, 3]
    assert find_smallest_sum(list1, list2) == 0

def test_find_smallest_sum_single_element():
    """Test with single-element lists"""
    list1 = [5]
    list2 = [2]
    assert find_smallest_sum(list1, list2) == 10

def test_find_smallest_sum_different_length_error():
    """Test that different length lists raise a ValueError"""
    with pytest.raises(ValueError, match="Input lists must have the same length"):
        find_smallest_sum([1, 2], [1, 2, 3])

def test_find_smallest_sum_non_list_error():
    """Test that non-list inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_sum(1, [1, 2])
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_sum([1, 2], "not a list")