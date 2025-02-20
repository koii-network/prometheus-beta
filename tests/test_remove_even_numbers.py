import pytest
from src.remove_even_numbers import remove_even_and_sum

def test_remove_even_numbers_basic():
    numbers = [1, 2, 3, 4, 5, 6]
    result = remove_even_and_sum(numbers)
    assert result == 12  # 2 + 4 + 6
    assert numbers == [1, 3, 5]  # Only odd numbers remain

def test_remove_even_numbers_empty_list():
    numbers = []
    result = remove_even_and_sum(numbers)
    assert result == 0
    assert numbers == []

def test_remove_even_numbers_only_odds():
    numbers = [1, 3, 5, 7]
    result = remove_even_and_sum(numbers)
    assert result == 0
    assert numbers == [1, 3, 5, 7]

def test_remove_even_numbers_only_evens():
    numbers = [2, 4, 6, 8]
    result = remove_even_and_sum(numbers)
    assert result == 20
    assert numbers == []

def test_remove_even_numbers_invalid_input():
    with pytest.raises(TypeError):
        remove_even_and_sum("not a list")
    with pytest.raises(TypeError):
        remove_even_and_sum(123)
    with pytest.raises(TypeError):
        remove_even_and_sum(None)