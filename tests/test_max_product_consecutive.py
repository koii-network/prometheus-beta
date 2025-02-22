import pytest
from src.max_product_consecutive import find_max_product_three_consecutive

def test_standard_positive_array():
    arr = [1, 2, 3, 4, 5]
    assert find_max_product_three_consecutive(arr) == 60  # 3 * 4 * 5

def test_array_with_negatives():
    arr = [-10, -3, 5, 6, -2]
    assert find_max_product_three_consecutive(arr) == 180  # -10 * -3 * 6

def test_array_with_zeros():
    arr = [0, 1, 2, 3, 0]
    assert find_max_product_three_consecutive(arr) == 6  # 1 * 2 * 3

def test_array_with_large_mixed_numbers():
    arr = [-100, 10, -5, 200, 3, 4, -1000]
    assert find_max_product_three_consecutive(arr) == 24000  # -5 * 200 * 3

def test_too_small_array():
    with pytest.raises(ValueError, match="Array must contain at least 3 elements"):
        find_max_product_three_consecutive([1, 2])

def test_minimum_length_array():
    arr = [1, 2, 3]
    assert find_max_product_three_consecutive(arr) == 6  # 1 * 2 * 3

def test_large_numbers():
    arr = [10000, 20000, 30000, 1, 2, 3]
    assert find_max_product_three_consecutive(arr) == 18000000000  # 10000 * 20000 * 30000