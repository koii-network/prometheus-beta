import pytest
from src.two_sum import two_sum

def test_two_sum_basic_true():
    """Test basic case where two numbers sum to target"""
    assert two_sum([1, 2, 3, 4, 5], 7) == True

def test_two_sum_basic_false():
    """Test case where no two numbers sum to target"""
    assert two_sum([1, 2, 3, 4, 5], 20) == False

def test_two_sum_duplicate_numbers():
    """Test case with duplicate numbers"""
    assert two_sum([3, 3], 6) == True

def test_two_sum_empty_list():
    """Test empty list case"""
    assert two_sum([], 5) == False

def test_two_sum_single_element():
    """Test list with single element"""
    assert two_sum([5], 10) == False

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-1, -2, -3, -4, -5], -8) == True

def test_two_sum_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert two_sum([-5, 0, 2, 3, 5, 7], 2) == True

def test_two_sum_float_numbers():
    """Test with floating point numbers"""
    assert two_sum([1.5, 2.5, 3.5], 5.0) == True

def test_two_sum_invalid_input_not_list():
    """Test invalid input type (not a list)"""
    with pytest.raises(TypeError, match="Input must be a list"):
        two_sum(123, 5)

def test_two_sum_invalid_target():
    """Test invalid target type"""
    with pytest.raises(TypeError, match="Target must be a number"):
        two_sum([1, 2, 3], "5")