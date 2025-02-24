import pytest
from src.array_sorter import sort_array_with_even_squares

def test_basic_sorting():
    """Test basic sorting with mix of even and odd numbers."""
    input_arr = [3, 1, 2, 4, 5]
    expected = [1, 3, 5, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_all_odd_numbers():
    """Test array with only odd numbers."""
    input_arr = [7, 3, 1, 5]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_all_even_numbers():
    """Test array with only even numbers."""
    input_arr = [4, 2, 6, 8]
    expected = [64, 36, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_empty_array():
    """Test empty input array."""
    assert sort_array_with_even_squares([]) == []

def test_negative_numbers():
    """Test array with negative numbers."""
    input_arr = [-3, -1, -2, -4, -5]
    expected = [-5, -3, -1, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_mixed_negative_and_positive():
    """Test array with mixed negative and positive numbers."""
    input_arr = [-3, 1, -2, 4, -5]
    expected = [-5, -3, 1, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_input_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_array_with_even_squares("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_array_with_even_squares(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_array_with_even_squares(None)