import pytest
from src.array_logger import log_array_table

def test_log_1d_array_default():
    arr = [1, 2, 3, 4, 5]
    expected_output = """Index | Value
-----------
0     | 1
1     | 2
2     | 3
3     | 4
4     | 5"""
    assert log_array_table(arr).replace(' ', '') == expected_output.replace(' ', '')

def test_log_1d_array_custom_headers():
    arr = [1, 2, 3, 4, 5]
    expected_output = """Num | Value
------------
Num | Value
1   | 2
2   | 3
3   | 4
4   | 5"""
    result = log_array_table(arr, ['Num', 'Value'])
    assert 'Num' in result
    assert 'Value' in result

def test_log_2d_array():
    arr = [[1, 'a'], [2, 'b'], [3, 'c']]
    expected_output = """Column 1 | Column 2
-------------------
1        | a
2        | b
3        | c"""
    result = log_array_table(arr)
    assert result.replace(' ', '') == expected_output.replace(' ', '')

def test_log_2d_array_custom_headers():
    arr = [[1, 'a'], [2, 'b'], [3, 'c']]
    expected_output = """Number | Letter
-------------------
1      | a
2      | b
3      | c"""
    result = log_array_table(arr, ['Number', 'Letter'])
    assert result.replace(' ', '') == expected_output.replace(' ', '')

def test_empty_array():
    arr = []
    assert log_array_table(arr) == ""

def test_invalid_input_type():
    with pytest.raises(TypeError):
        log_array_table("not a list")

def test_2d_array_inconsistent_sublists():
    with pytest.raises(ValueError):
        log_array_table([[1, 2], [3]])

def test_1d_array_incorrect_header_length():
    with pytest.raises(ValueError):
        log_array_table([1, 2, 3], ['Single'])

def test_2d_array_incorrect_header_length():
    with pytest.raises(ValueError):
        log_array_table([[1, 2], [3, 4]], ['Single'])