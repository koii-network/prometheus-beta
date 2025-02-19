import pytest
from src.string_utils import convert_to_inverse_case

def test_convert_to_inverse_case_normal_string():
    """Test conversion of a regular mixed-case string."""
    assert convert_to_inverse_case('Hello World') == 'hELLO wORLD'

def test_convert_to_inverse_case_all_uppercase():
    """Test conversion of an all-uppercase string."""
    assert convert_to_inverse_case('HELLO') == 'hello'

def test_convert_to_inverse_case_all_lowercase():
    """Test conversion of an all-lowercase string."""
    assert convert_to_inverse_case('python') == 'PYTHON'

def test_convert_to_inverse_case_with_numbers_and_symbols():
    """Test conversion of a string with numbers and symbols."""
    assert convert_to_inverse_case('Hello123! World') == 'hELLO123! wORLD'

def test_convert_to_inverse_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_inverse_case('') == ''

def test_convert_to_inverse_case_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(123)
        convert_to_inverse_case(None)