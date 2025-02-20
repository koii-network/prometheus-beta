import pytest
from src.even_number_remover import remove_evens_and_sum

def test_remove_evens_and_sum_normal_case():
    nums = [1, 2, 3, 4, 5, 6]
    result = remove_evens_and_sum(nums)
    assert result == 12  # 2 + 4 + 6
    assert nums == [1, 3, 5]  # Only odd numbers remain

def test_remove_evens_and_sum_no_evens():
    nums = [1, 3, 5, 7]
    result = remove_evens_and_sum(nums)
    assert result == 0
    assert nums == [1, 3, 5, 7]

def test_remove_evens_and_sum_only_evens():
    nums = [2, 4, 6, 8]
    result = remove_evens_and_sum(nums)
    assert result == 20
    assert nums == []

def test_remove_evens_and_sum_empty_list():
    nums = []
    result = remove_evens_and_sum(nums)
    assert result == 0
    assert nums == []

def test_remove_evens_and_sum_mixed_signs():
    nums = [-1, -2, 0, 3, 4, -5]
    result = remove_evens_and_sum(nums)
    assert result == -2 + 0 + 4
    assert nums == [-1, 3, -5]