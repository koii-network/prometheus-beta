import pytest
from src.inverse_case import convert_to_inverse_case

def test_convert_to_inverse_case_basic():
    assert convert_to_inverse_case("Hello World") == "hELLO wORLD"
    assert convert_to_inverse_case("Python") == "pYTHON"
    assert convert_to_inverse_case("OpenAI") == "oPENai"

def test_convert_to_inverse_case_empty_string():
    assert convert_to_inverse_case("") == ""

def test_convert_to_inverse_case_numbers_and_symbols():
    assert convert_to_inverse_case("Hello123!") == "hELLO123!"
    assert convert_to_inverse_case("UPPER lower 42") == "upper LOWER 42"

def test_convert_to_inverse_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_inverse_case(None)
    with pytest.raises(TypeError):
        convert_to_inverse_case(123)