import pytest
from src.array_table_logger import log_array_as_table

def test_log_array_1d():
    # Test 1D array without headers
    arr = [1, 2, 3, 4, 5]
    expected_output = (
        "0 | \n"
        "-----\n"
        "1 | \n"
        "2 | \n"
        "3 | \n"
        "4 | "
    )
    assert log_array_as_table(arr).replace(" ", "") == expected_output.replace(" ", "")

def test_log_array_2d():
    # Test 2D array with headers
    arr = [[1, 'a'], [2, 'b'], [3, 'c']]
    headers = ['Number', 'Letter']
    expected_output = (
        "Number | Letter\n"
        "---------------\n"
        "1      | a      \n"
        "2      | b      \n"
        "3      | c      "
    )
    assert log_array_as_table(arr, headers) == expected_output

def test_log_array_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        log_array_as_table("not a list")
    
    # Test mismatched headers
    with pytest.raises(ValueError):
        log_array_as_table([[1, 2], [3, 4]], headers=['Single'])

def test_log_array_empty():
    # Test empty array
    assert log_array_as_table([]) == ""

def test_log_array_complex_types():
    # Test array with complex types
    arr = [[1, 'hello'], [2, 'world'], [3, {'key': 'value'}]]
    headers = ['ID', 'Data']
    result = log_array_as_table(arr, headers)
    assert isinstance(result, str)
    assert 'ID' in result
    assert 'Data' in result
    assert 'hello' in result
    assert "'key': 'value'" in result