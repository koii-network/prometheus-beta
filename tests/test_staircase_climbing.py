import pytest
from src.staircase_climbing import count_staircase_ways

def test_basic_staircase():
    # A simple staircase with total height of 4
    assert count_staircase_ways([2, 2]) == 3
    
def test_single_step_staircase():
    # Total height 1
    assert count_staircase_ways([1]) == 1
    
def test_long_staircase():
    # More complex staircase
    assert count_staircase_ways([1, 1, 1, 1]) == 5
    
def test_mixed_step_lengths():
    # Staircase with varying step lengths
    assert count_staircase_ways([3, 2]) == 3
    
def test_invalid_input_empty_list():
    with pytest.raises(ValueError):
        count_staircase_ways([])
        
def test_invalid_input_negative_length():
    with pytest.raises(ValueError):
        count_staircase_ways([-1, 2, 3])
        
def test_invalid_input_zero_length():
    with pytest.raises(ValueError):
        count_staircase_ways([0, 2, 3])