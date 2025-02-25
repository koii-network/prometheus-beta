import pytest
from src.staircase_climbing import count_climbing_ways

def test_basic_staircase_lengths():
    """Test basic staircase length scenarios"""
    assert count_climbing_ways([1, 2, 3]) == [1, 2, 3], "Basic staircase length calculation failed"

def test_zero_and_negative_lengths():
    """Test handling of zero and negative lengths"""
    assert count_climbing_ways([0, 4, 5]) == [0, 5, 8], "Zero and positive length handling failed"

def test_large_staircase_length():
    """Test a larger staircase length"""
    result = count_climbing_ways([10])
    assert result == [89], "Large staircase length calculation incorrect"

def test_multiple_staircases():
    """Test multiple staircase lengths in one call"""
    assert count_climbing_ways([1, 2, 3, 4, 5]) == [1, 2, 3, 5, 8], "Multiple staircase lengths failed"

def test_invalid_input_type():
    """Test raising error for non-list input"""
    with pytest.raises(ValueError, match="Input must be a list of stair lengths"):
        count_climbing_ways(10)

def test_invalid_stair_lengths():
    """Test raising error for invalid stair lengths"""
    with pytest.raises(ValueError, match="Stair lengths must be non-negative integers"):
        count_climbing_ways([1, -2, 3])
    with pytest.raises(ValueError, match="Stair lengths must be non-negative integers"):
        count_climbing_ways([1, 2.5, 3])

def test_empty_list():
    """Test empty list input"""
    assert count_climbing_ways([]) == [], "Empty list handling failed"