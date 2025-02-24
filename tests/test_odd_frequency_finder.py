import pytest
from src.odd_frequency_finder import find_odd_frequency_number

def test_single_odd_frequency_number():
    assert find_odd_frequency_number([1, 1, 2, 2, 3]) == 3

def test_smallest_odd_frequency_number():
    assert find_odd_frequency_number([1, 1, 2, 2, 3, 3, 3]) == 3

def test_repeated_odd_frequency_number():
    assert find_odd_frequency_number([5, 5, 5, 1, 1, 2, 2]) == 5

def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_frequency_number([])

def test_no_odd_frequency_number_raises_error():
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_frequency_number([1, 1, 2, 2, 3, 3])

def test_large_numbers():
    assert find_odd_frequency_number([10000, 10000, 20000, 20000, 30000]) == 30000

def test_single_element_list():
    assert find_odd_frequency_number([42]) == 42

def test_complex_list():
    assert find_odd_frequency_number([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 3