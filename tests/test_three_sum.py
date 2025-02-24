import pytest
from src.three_sum import find_three_sum_triplets

def test_basic_three_sum():
    """Test basic scenario with multiple triplets"""
    nums = [1, 0, -1, 2, -2, 3]
    target = 2
    result = find_three_sum_triplets(nums, target)
    expected = [[-2, -1, 3], [-1, 0, 3], [-2, 1, 3], [0, 1, 1]]
    # Sort both result and expected to compare
    assert sorted(sorted(triplet) for triplet in result) == sorted(sorted(triplet) for triplet in expected)

def test_no_triplets():
    """Test case where no triplets sum to target"""
    nums = [1, 2, 3, 4, 5]
    target = 100
    result = find_three_sum_triplets(nums, target)
    assert result == []

def test_multiple_duplicate_triplets():
    """Test case with duplicate elements and multiple triplets"""
    nums = [1, 1, 1, 2, 2, 3, 3, 4]
    target = 6
    result = find_three_sum_triplets(nums, target)
    expected = [[1, 1, 4], [1, 2, 3], [2, 2, 2]]
    assert sorted(sorted(triplet) for triplet in result) == sorted(sorted(triplet) for triplet in expected)

def test_negative_numbers():
    """Test scenario with negative numbers"""
    nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    target = 0
    result = find_three_sum_triplets(nums, target)
    expected = [[-5, 0, 5], [-4, -1, 5], [-4, 0, 4], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], 
                [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    assert sorted(sorted(triplet) for triplet in result) == sorted(sorted(triplet) for triplet in expected)

def test_input_error_types():
    """Test input type validation"""
    with pytest.raises(TypeError):
        find_three_sum_triplets("not a list", 5)
    
    with pytest.raises(TypeError):
        find_three_sum_triplets([1, 2, 3], "not a number")

def test_insufficient_elements():
    """Test input list with insufficient elements"""
    with pytest.raises(ValueError):
        find_three_sum_triplets([1, 2], 5)

def test_empty_list():
    """Test empty input list"""
    with pytest.raises(ValueError):
        find_three_sum_triplets([], 5)