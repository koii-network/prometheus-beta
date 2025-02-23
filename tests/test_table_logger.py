import pytest
from src.table_logger import log_array_as_table

def test_simple_array_logging():
    # Test logging a simple 1D array
    result = log_array_as_table([1, 2, 3])
    expected = "0\n-\n1\n2\n3"
    assert result.replace(" ", "") == expected.replace(" ", "")

def test_2d_array_logging():
    # Test logging a 2D array
    data = [[1, 'a'], [2, 'b'], [3, 'c']]
    result = log_array_as_table(data)
    assert '1 | a' in result
    assert '2 | b' in result
    assert '3 | c' in result

def test_custom_headers():
    # Test logging with custom headers
    data = [[1, 'a'], [2, 'b'], [3, 'c']]
    result = log_array_as_table(data, headers=['Number', 'Letter'])
    assert 'Number | Letter' in result
    assert '1 | a' in result
    assert '3 | c' in result

def test_empty_array():
    # Test logging an empty array
    result = log_array_as_table([])
    assert result == "Empty table"

def test_invalid_input_type():
    # Test invalid input type
    with pytest.raises(TypeError):
        log_array_as_table("not a list")

def test_mismatched_headers():
    # Test headers that don't match array columns
    data = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError):
        log_array_as_table(data, headers=['A', 'B'])

def test_mixed_type_array():
    # Test array with mixed types
    data = [[1, 'a'], [True, 3.14], [None, 'test']]
    result = log_array_as_table(data)
    assert '1 | a' in result
    assert 'True | 3.14' in result
    assert 'None | test' in result