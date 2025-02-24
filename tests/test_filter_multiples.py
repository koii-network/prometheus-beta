import pytest
from src.filter_multiples import filter_exclusive_multiples

def test_basic_filtering():
    """Test basic filtering of exclusive multiples."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [3, 5, 6, 9, 10]
    assert filter_exclusive_multiples(input_list) == expected

def test_empty_list():
    """Test filtering an empty list."""
    assert filter_exclusive_multiples([]) == []

def test_no_exclusive_multiples():
    """Test a list with no exclusive multiples."""
    input_list = [1, 2, 4, 8]
    assert filter_exclusive_multiples(input_list) == []

def test_all_exclusive_multiples():
    """Test a list with only exclusive multiples."""
    input_list = [3, 5, 6, 9, 10]
    expected = [3, 5, 6, 9, 10]
    assert filter_exclusive_multiples(input_list) == expected

def test_sorting():
    """Test that the output is sorted."""
    input_list = [10, 3, 15, 6, 5]
    expected = [3, 5, 6, 10]
    assert filter_exclusive_multiples(input_list) == expected

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        filter_exclusive_multiples("not a list")
        filter_exclusive_multiples(123)
        filter_exclusive_multiples(None)