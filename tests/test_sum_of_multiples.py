import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic():
    """Test basic functionality with simple inputs"""
    assert sum_of_multiples(3, 5) == 33

def test_sum_of_multiples_same_number():
    """Test when both inputs are the same"""
    assert sum_of_multiples(7, 7) == 14 + 21 + 28 + 35 + 42 + 49 + 56 + 63 + 70 + 77 + 84 + 91 + 98

def test_sum_of_multiples_edge_cases():
    """Test edge cases of range 1 to 100"""
    assert sum_of_multiples(1, 100) == sum(range(1, 101))

def test_sum_of_multiples_invalid_input_low():
    """Test input validation for low values"""
    with pytest.raises(ValueError):
        sum_of_multiples(0, 5)

def test_sum_of_multiples_invalid_input_high():
    """Test input validation for high values"""
    with pytest.raises(ValueError):
        sum_of_multiples(101, 5)

def test_sum_of_multiples_no_duplicates():
    """Ensure no duplicates are counted"""
    # Multiples of 3 in the range 1-100: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99
    # Multiples of 5 in the range 1-100: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100
    assert sum_of_multiples(3, 5) == 33 + 5 + 10 + 20 + 25 + 40 + 50 + 55 + 65 + 70 + 80 + 85 + 95 + 100