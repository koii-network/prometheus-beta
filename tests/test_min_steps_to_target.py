import pytest
from src.min_steps_to_target import min_steps_to_target_sum

def test_basic_positive_scenario():
    """Test basic scenario with positive numbers."""
    numbers = [1, 2, 3, 4, 5]
    target = 7
    assert min_steps_to_target_sum(numbers, target) == 2

def test_exact_match():
    """Test when a number exactly matches the target."""
    numbers = [1, 2, 3, 7, 5]
    target = 7
    assert min_steps_to_target_sum(numbers, target) == 1

def test_negative_numbers():
    """Test scenario with negative numbers."""
    numbers = [-1, -2, 3, 4, 5]
    target = 2
    assert min_steps_to_target_sum(numbers, target) == 2

def test_complex_combination():
    """Test a more complex combination of steps."""
    numbers = [10, 5, 3, 7, 2]
    target = 12
    assert min_steps_to_target_sum(numbers, target) == 2

def test_impossible_target():
    """Test when target cannot be reached."""
    numbers = [1, 2, 3]
    target = 100
    assert min_steps_to_target_sum(numbers, target) == -1

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError."""
    with pytest.raises(ValueError):
        min_steps_to_target_sum([], 5)

def test_zero_target():
    """Test reaching a zero target."""
    numbers = [-1, 1, 2, -2]
    target = 0
    assert min_steps_to_target_sum(numbers, target) == 1

def test_multiple_paths():
    """Test scenario with multiple possible paths."""
    numbers = [1, 3, 4, 5]
    target = 7
    assert min_steps_to_target_sum(numbers, target) in [2, 1]