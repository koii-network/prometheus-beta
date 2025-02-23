import pytest
from src.equal_sum_partition import can_partition_into_equal_sum_sublists

def test_can_partition_basic_true():
    """Test a basic case where partitioning is possible."""
    assert can_partition_into_equal_sum_sublists([1, 5, 11, 5]) == True

def test_can_partition_basic_false():
    """Test a basic case where partitioning is not possible."""
    assert can_partition_into_equal_sum_sublists([1, 2, 3, 5]) == False

def test_can_partition_empty_list():
    """Test behavior with an empty list."""
    assert can_partition_into_equal_sum_sublists([]) == False

def test_can_partition_single_element():
    """Test behavior with a single element."""
    assert can_partition_into_equal_sum_sublists([1]) == False

def test_can_partition_negative_numbers():
    """Test with a mix of negative and positive numbers."""
    assert can_partition_into_equal_sum_sublists([-1, 1, 0, 2, -2]) == True

def test_can_partition_all_zeros():
    """Test with a list of zeros."""
    assert can_partition_into_equal_sum_sublists([0, 0, 0, 0]) == True

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        can_partition_into_equal_sum_sublists("not a list")

def test_invalid_list_contents():
    """Test that ValueError is raised for non-integer list contents."""
    with pytest.raises(ValueError):
        can_partition_into_equal_sum_sublists([1, 2, "3", 4])

def test_large_numbers():
    """Test with larger numbers."""
    assert can_partition_into_equal_sum_sublists([100, 100, 100, 100, 100, 100]) == True

def test_complex_partition():
    """Test a more complex partitioning scenario."""
    assert can_partition_into_equal_sum_sublists([1, 3, 4, 8]) == True