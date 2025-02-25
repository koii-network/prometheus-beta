import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list():
    """Test with an odd-length list"""
    test_list = [1, 2, 3, 4, 5, 6, 7]
    assert find_middle_range_indices(test_list, 1) == [2, 3, 4]
    assert find_middle_range_indices(test_list, 0) == [3]

def test_even_length_list():
    """Test with an even-length list"""
    test_list = [1, 2, 3, 4, 5, 6]
    assert find_middle_range_indices(test_list, 1) == [2, 3]
    assert find_middle_range_indices(test_list, 0) == [2]

def test_range_width_zero():
    """Test with range width of zero"""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, 0) == [2]

def test_range_width_exceeds_list():
    """Test when range width is larger than the list"""
    test_list = [1, 2, 3]
    assert find_middle_range_indices(test_list, 5) == [0, 1, 2]

def test_empty_list():
    """Test with an empty list"""
    assert find_middle_range_indices([], 2) == []

def test_negative_range_width():
    """Test raising error for negative range width"""
    with pytest.raises(ValueError):
        find_middle_range_indices([1, 2, 3], -1)

def test_invalid_input_types():
    """Test raising error for invalid input types"""
    with pytest.raises(TypeError):
        find_middle_range_indices("not a list", 2)
    
    with pytest.raises(TypeError):
        find_middle_range_indices([1, 2, 3], "not an int")