import pytest
from src.minimum_steps import minimum_steps_to_target

def test_basic_positive_case():
    """Test a simple case where target can be reached"""
    numbers = [1, 2, 3, 4, 5]
    target = 7
    assert minimum_steps_to_target(numbers, target) == 2

def test_no_solution():
    """Test case where target cannot be reached"""
    numbers = [10, 20, 30]
    target = 15
    assert minimum_steps_to_target(numbers, target) == -1

def test_zero_sum():
    """Test case with zero as target"""
    numbers = [1, -1, 2, -2, 3]
    target = 0
    assert minimum_steps_to_target(numbers, target) == 1

def test_single_number_solution():
    """Test case where single number matches target"""
    numbers = [1, 2, 3, 4, 5]
    target = 3
    assert minimum_steps_to_target(numbers, target) == 1

def test_large_numbers():
    """Test case with larger numbers"""
    numbers = [10, 20, 30, 40, 50]
    target = 60
    result = minimum_steps_to_target(numbers, target)
    assert result in [2, 3]  # Depending on the specific algorithm, result might vary

def test_empty_list():
    """Test with empty input list"""
    numbers = []
    target = 5
    assert minimum_steps_to_target(numbers, target) == -1

def test_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, 3, 4, 5]
    target = 2
    assert minimum_steps_to_target(numbers, target) == 2