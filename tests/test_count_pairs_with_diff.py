import pytest
from src.count_pairs_with_diff import count_pairs_with_difference_of_five

def test_basic_pairs_with_difference():
    """Test basic scenarios with pairs having a difference of 5."""
    assert count_pairs_with_difference_of_five([1, 6, 3, 8, 2, 7]) == 3
    assert count_pairs_with_difference_of_five([5, 10, 15, 20]) == 3
    assert count_pairs_with_difference_of_five([]) == 0

def test_pairs_with_multiple_arrangements():
    """Test different arrangements of pairs with difference of 5."""
    assert count_pairs_with_difference_of_five([0, 5, 10, 15, 20]) == 4
    assert count_pairs_with_difference_of_five([5, 0, 10, 15, 20]) == 4

def test_no_pairs_with_difference():
    """Test list with no pairs having a difference of 5."""
    assert count_pairs_with_difference_of_five([1, 2, 3, 4, 5]) == 0

def test_duplicate_values():
    """Test list with duplicate values."""
    assert count_pairs_with_difference_of_five([5, 5, 10, 10, 15, 15]) == 3

def test_negative_numbers():
    """Test list with negative numbers."""
    assert count_pairs_with_difference_of_five([-5, 0, 5, 10, -10, -5]) == 4

def test_invalid_input_type():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        count_pairs_with_difference_of_five("not a list")
    with pytest.raises(TypeError):
        count_pairs_with_difference_of_five(123)

def test_invalid_list_contents():
    """Test list with non-integer elements raises ValueError."""
    with pytest.raises(ValueError):
        count_pairs_with_difference_of_five([1, 2, "3", 4])
    with pytest.raises(ValueError):
        count_pairs_with_difference_of_five([1.5, 6.5, 2.5])