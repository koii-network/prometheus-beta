import pytest
from src.remove_even_numbers import remove_even_numbers

def test_remove_even_numbers_standard_case():
    result, even_sum = remove_even_numbers([1, 2, 3, 4, 5, 6])
    assert result == [1, 3, 5]
    assert even_sum == 12

def test_remove_even_numbers_all_even():
    result, even_sum = remove_even_numbers([2, 4, 6, 8])
    assert result == []
    assert even_sum == 20

def test_remove_even_numbers_all_odd():
    result, even_sum = remove_even_numbers([1, 3, 5, 7])
    assert result == [1, 3, 5, 7]
    assert even_sum == 0

def test_remove_even_numbers_empty_list():
    result, even_sum = remove_even_numbers([])
    assert result == []
    assert even_sum == 0

def test_remove_even_numbers_invalid_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_even_numbers("not a list")

def test_remove_even_numbers_invalid_element():
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_even_numbers([1, 2, "3", 4])