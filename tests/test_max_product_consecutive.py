import pytest
from src.max_product_consecutive import find_max_product_consecutive

def test_normal_positive_array():
    arr = [1, 2, 3, 4, 5]
    assert find_max_product_consecutive(arr) == 60  # 3 * 4 * 5

def test_array_with_negatives():
    arr = [-1, -2, -3, 4, 5]
    assert find_max_product_consecutive(arr) == 30  # -2 * -3 * 5

def test_mixed_values():
    arr = [0, -1, 2, 3, -4]
    assert find_max_product_consecutive(arr) == 6  # 2 * 3 * 1

def test_small_array():
    arr = [1, 2]
    assert find_max_product_consecutive(arr) is None

def test_empty_array():
    arr = []
    assert find_max_product_consecutive(arr) is None

def test_large_values():
    arr = [1000000, -1000000, 1000000, 2, 3]
    assert find_max_product_consecutive(arr) == 1000000 * -1000000 * 1000000

def test_all_zeros():
    arr = [0, 0, 0, 0, 0]
    assert find_max_product_consecutive(arr) == 0

def test_first_three_max():
    arr = [10, 5, 3, 2, 1]
    assert find_max_product_consecutive(arr) == 10 * 5 * 3

def test_last_three_max():
    arr = [1, 2, 3, 10, 5]
    assert find_max_product_consecutive(arr) == 3 * 10 * 5