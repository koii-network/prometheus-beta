import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic_scenarios():
    # Basic test cases with known solutions
    assert rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 4) == 10
    assert rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8) == 22

def test_rod_cutting_edge_cases():
    # Edge case tests
    assert rod_cutting([], 5) == 0
    assert rod_cutting([1, 2, 3], 0) == 0
    assert rod_cutting([1], 1) == 1
    assert rod_cutting([1], 3) == 3

def test_rod_cutting_different_lengths():
    # Test with different pricing and rod lengths
    assert rod_cutting([3, 5, 8, 9, 10, 17, 17, 20], 5) == 15
    assert rod_cutting([1, 2, 3, 4, 5], 5) == 10

def test_rod_cutting_invalid_input():
    # Test invalid input scenarios
    with pytest.raises(ValueError):
        rod_cutting([-1, 2, 3], 3)
    
    # Test input where prices list is shorter than length
    assert rod_cutting([1, 5, 8], 5) == 13

def test_rod_cutting_single_length():
    # Test scenarios with single length pieces
    assert rod_cutting([1], 5) == 5
    assert rod_cutting([10], 3) == 30

def test_rod_cutting_complex_scenario():
    # More complex pricing scenario
    prices = [2, 5, 7, 8, 10, 12, 15, 18, 20, 22]
    assert rod_cutting(prices, 6) == 15  # Updated expected value