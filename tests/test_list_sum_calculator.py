import pytest
from src.list_sum_calculator import calculate_sum

def test_calculate_sum_normal_case():
    """Test normal list with positive integers."""
    test_list = [1, 2, 3, 4, 5]
    assert calculate_sum(test_list) == 40  # 0*1 + 1*2 + 2*3 + 3*4 + 4*5 = 40

def test_calculate_sum_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_with_zeros():
    """Test list containing zeros."""
    test_list = [0, 0, 0, 0]
    assert calculate_sum(test_list) == 0

def test_calculate_sum_with_negative_numbers():
    """Test list with negative numbers."""
    test_list = [-1, -2, -3, -4, -5]
    assert calculate_sum(test_list) == -40  # 0*(-1) + 1*(-2) + 2*(-3) + 3*(-4) + 4*(-5) = -40

def test_calculate_sum_invalid_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum(123)

def test_calculate_sum_invalid_elements():
    """Test that ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All list elements must be integers"):
        calculate_sum([1, 2, "3", 4])
    with pytest.raises(ValueError, match="All list elements must be integers"):
        calculate_sum([1, 2, 3.5, 4])