import pytest
from src.array_processor import process_array

def test_basic_processing():
    """Test basic functionality of the array processor"""
    # In [2, 4, 6, 8, 10], 6 will be multiplied by 2, 
    # and even numbers 2, 4, 8, 10 will be summed
    assert process_array([2, 4, 6, 8, 10]) == 24

def test_empty_list():
    """Test processing an empty list"""
    assert process_array([]) == 0

def test_no_even_numbers():
    """Test list with no even numbers"""
    assert process_array([1, 3, 5, 7, 9]) == 0

def test_modified_number_exclusion():
    """Ensure modified numbers are not included in sum"""
    # [2, 4, 12, 8, 10] - 12 is modified (6*2), so not included in sum
    assert process_array([2, 4, 6, 8, 10]) == 24

def test_floating_point_numbers():
    """Test with floating point numbers"""
    assert process_array([2.0, 4.0, 6.0, 8.0, 10.0]) == 24.0

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        process_array("not a list")

def test_non_numeric_elements():
    """Test raising ValueError for non-numeric elements"""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        process_array([1, 2, "three", 4, 5])

def test_single_element_lists():
    """Test processing lists with few elements"""
    assert process_array([2]) == 2
    assert process_array([3]) == 0

def test_large_list():
    """Test processing a larger list"""
    test_list = list(range(1, 21))  # 1 to 20
    # Manually calculate expected result
    expected = sum(num for i, num in enumerate(test_list) if i % 3 != 2 and num % 2 == 0)
    assert process_array(test_list) == expected