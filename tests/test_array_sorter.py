import pytest
from src.array_sorter import sort_array_with_even_squares

def test_basic_sorting():
    """Test basic sorting functionality"""
    input_arr = [3, 1, 2, 4, 5]
    expected = [1, 3, 5, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_empty_list():
    """Test empty list input"""
    assert sort_array_with_even_squares([]) == []

def test_no_even_numbers():
    """Test list with only odd numbers"""
    input_arr = [7, 3, 1, 5]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_only_even_numbers():
    """Test list with only even numbers"""
    input_arr = [4, 2, 6, 8]
    expected = [4, 64, 36, 16]
    assert sort_array_with_even_squares(input_arr) == expected

def test_negative_numbers():
    """Test list with negative numbers"""
    input_arr = [-3, -1, -2, -4, 5]
    expected = [-3, -1, 5, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        sort_array_with_even_squares("not a list")
        
def test_mixed_numbers():
    """Test mixed positive and negative numbers"""
    input_arr = [3, -2, 1, 4, -1, 5]
    expected = [-1, 1, 3, 5, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected