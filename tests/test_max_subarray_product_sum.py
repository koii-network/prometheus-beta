import pytest
from src.max_subarray_product_sum import find_max_subarray_product_sum

def test_basic_scenario():
    assert find_max_subarray_product_sum([1, 2, 3, 4], 6) == 5  # [2, 3]
    assert find_max_subarray_product_sum([1, 2, 3, 4], 12) == 7  # [3, 4]

def test_single_element():
    assert find_max_subarray_product_sum([3], 3) == 3
    assert find_max_subarray_product_sum([5], 5) == 5

def test_product_at_end():
    assert find_max_subarray_product_sum([1, 2, 3, 2], 6) == 5  # [2, 3]

def test_multiple_subarrays():
    assert find_max_subarray_product_sum([1, 2, 3, 4, 3, 2], 6) == 7  # max between [2, 3] and [3, 2]

def test_no_matching_subarray():
    assert find_max_subarray_product_sum([1, 2, 3, 4], 100) == -1

def test_invalid_input():
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_product_sum([], 10)
    
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_subarray_product_sum([1, 2, -3, 4], 6)
        
def test_larger_array():
    assert find_max_subarray_product_sum([1, 2, 3, 4, 5, 6], 24) == 15  # [4, 5, 6]