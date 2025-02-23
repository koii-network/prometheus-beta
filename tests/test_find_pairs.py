import pytest
from src.find_pairs import find_pairs_sum_to_target

def test_basic_pairs():
    """Test finding basic pairs that sum to target"""
    assert set(find_pairs_sum_to_target([1, 2, 3, 4, 5], 7)) == {(2, 5), (3, 4)}

def test_pairs_with_negative_numbers():
    """Test pairs with negative numbers"""
    assert set(find_pairs_sum_to_target([-1, 0, 1, 2, -2], 0)) == {(-1, 1), (-2, 2)}

def test_duplicate_numbers():
    """Test handling of duplicate numbers"""
    assert set(find_pairs_sum_to_target([1, 1, 2, 2, 3, 3], 4)) == {(1, 3), (2, 2)}

def test_no_pairs_found():
    """Test case where no pairs sum to target"""
    assert find_pairs_sum_to_target([1, 2, 3, 4], 10) == []

def test_floating_point_numbers():
    """Test pairs with floating point numbers"""
    assert set(find_pairs_sum_to_target([1.5, 2.5, 3.0, 4.0], 5.5)) == {(1.5, 4.0), (2.5, 3.0)}

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_pairs_sum_to_target("not a list", 10)

def test_invalid_target_type():
    """Test raising TypeError for invalid target type"""
    with pytest.raises(TypeError, match="Target must be a number"):
        find_pairs_sum_to_target([1, 2, 3], "not a number")

def test_invalid_list_elements():
    """Test raising ValueError for list with non-numeric elements"""
    with pytest.raises(ValueError, match="List contains elements that cannot be used in arithmetic"):
        find_pairs_sum_to_target([1, 2, "three"], 5)

def test_empty_list():
    """Test behavior with an empty list"""
    assert find_pairs_sum_to_target([], 5) == []