import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_case():
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    arr = [5]
    k = 1
    assert max_subarray_sum(arr, k) == 5

def test_all_same_elements():
    arr = [2, 2, 2, 2, 2]
    k = 3
    assert max_subarray_sum(arr, k) == 6

def test_negative_numbers():
    arr = [-1, -2, -3, 4, -5, 6, -7]
    k = 3
    assert max_subarray_sum(arr, k) == 5  # 4 + (-5) + 6 = 5

def test_edge_cases():
    # Empty array
    with pytest.raises(ValueError):
        max_subarray_sum([], 1)
    
    # k larger than array length
    with pytest.raises(ValueError):
        max_subarray_sum([1, 2, 3], 4)
    
    # k is zero or negative
    with pytest.raises(ValueError):
        max_subarray_sum([1, 2, 3], 0)
    
    with pytest.raises(ValueError):
        max_subarray_sum([1, 2, 3], -1)

def test_input_type_errors():
    # Non-list input
    with pytest.raises(TypeError):
        max_subarray_sum(123, 2)
    
    # Non-integer k
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, 3], "2")