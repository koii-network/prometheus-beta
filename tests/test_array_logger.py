import pytest
from src.array_logger import log_array_table

def test_basic_array_logging():
    # Test basic 1D array
    result = log_array_table([1, 2, 3])
    assert 'Column 1' in result
    assert '1' in result
    assert '2' in result
    assert '3' in result

def test_nested_array_logging():
    # Test nested array with multiple columns
    result = log_array_table([[1, 'a'], [2, 'b'], [3, 'c']])
    assert 'Column 1' in result
    assert 'Column 2' in result
    assert '1' in result
    assert 'a' in result
    assert any('1' in line and 'a' in line for line in result.split('\n'))

def test_custom_headers():
    # Test with custom headers
    result = log_array_table([[1, 'a'], [2, 'b']], headers=['Number', 'Letter'])
    assert 'Number | Letter' in result
    assert '1' in result
    assert 'a' in result
    assert any('1' in line and 'a' in line for line in result.split('\n'))

def test_empty_array():
    # Test empty array returns empty string
    result = log_array_table([])
    assert result == ''

def test_mixed_type_array():
    # Test array with mixed types
    result = log_array_table([1, 'string', [3, 4], {'key': 'value'}])
    assert 'Column 1' in result
    assert '1' in result
    assert 'string' in result
    assert '[3, 4]' in result or '3' in result
    assert "{'key': 'value'}" in result

def test_indentation():
    # Test indentation
    result = log_array_table([1, 2, 3], indent=4)
    assert result.startswith('    ')

def test_invalid_headers():
    # Test headers length mismatch
    with pytest.raises(ValueError):
        log_array_table([[1, 2], [3, 4]], headers=['Single'])

def test_type_error():
    # Test non-list input
    with pytest.raises(TypeError):
        log_array_table("not a list")