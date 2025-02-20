import pytest
from src.unique_even_sum import sum_unique_even_numbers

def test_unique_even_numbers_basic():
    # Basic case with unique even numbers
    assert sum_unique_even_numbers([2, 4, 6, 8]) == 20

def test_unique_even_numbers_with_duplicates():
    # Numbers that appear more than once should be excluded
    assert sum_unique_even_numbers([2, 2, 4, 6, 8, 8]) == 6

def test_mixed_numbers():
    # Mix of even and odd numbers, some unique some not
    assert sum_unique_even_numbers([1, 2, 3, 4, 4, 5, 6, 7, 8]) == 2

def test_empty_array():
    # Empty array should return 0
    assert sum_unique_even_numbers([]) == 0

def test_no_even_numbers():
    # Array with only odd numbers
    assert sum_unique_even_numbers([1, 3, 5, 7]) == 0

def test_negative_even_numbers():
    # Array with negative even numbers
    assert sum_unique_even_numbers([-2, 2, -4, 4, -6]) == -2

def test_large_numbers():
    # Large numbers, some unique some not
    assert sum_unique_even_numbers([1000, 1000, 2000, 3000, 3000]) == 2000