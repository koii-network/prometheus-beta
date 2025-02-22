import pytest
from src.median_finder import find_median

def test_median_odd_length_list():
    numbers = [1, 3, 5, 7, 9]
    assert find_median(numbers) == 5

def test_median_even_length_list():
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_median(numbers) == 3.5

def test_median_single_element():
    numbers = [42]
    assert find_median(numbers) == 42.0

def test_median_with_floating_point_numbers():
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    assert find_median(numbers) == 3.5

def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="Cannot find median of an empty list"):
        find_median([])

def test_non_list_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median(42)

def test_non_numeric_list_raises_error():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_median([1, 2, 'three', 4])