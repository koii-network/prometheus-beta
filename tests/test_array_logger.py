import pytest
from src.array_logger import log_array_table

def test_1d_array_default_headers():
    """Test logging a 1D array with default headers."""
    arr = [1, 2, 3, 4, 5]
    result = log_array_table(arr)
    assert "Column 1" in result
    assert all(str(x) in result for x in arr)

def test_2d_array_with_custom_headers():
    """Test logging a 2D array with custom headers."""
    arr = [[1, 'a'], [2, 'b'], [3, 'c']]
    headers = ['Number', 'Letter']
    result = log_array_table(arr, headers)
    assert 'Number' in result
    assert 'Letter' in result
    assert all(str(x) in result for sublist in arr for x in sublist)

def test_single_element_array():
    """Test logging an array with a single element."""
    arr = [42]
    result = log_array_table(arr)
    assert '42' in result

def test_input_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        log_array_table("not a list")

def test_empty_array_error():
    """Test that a ValueError is raised for an empty array."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        log_array_table([])

def test_headers_mismatch_error():
    """Test that a ValueError is raised when headers don't match array columns."""
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Number of headers must match number of columns"):
        log_array_table(arr, headers=['Single Header'])

def test_mixed_type_array():
    """Test logging an array with mixed data types."""
    arr = [1, 'two', 3.0, [4]]
    result = log_array_table(arr)
    assert all(str(x) in result for x in arr)