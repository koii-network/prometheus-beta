import pytest
from src.inverse_case import convert_to_inverse_case

def test_convert_to_inverse_case_basic():
    assert convert_to_inverse_case("Hello") == "hELLO"
    assert convert_to_inverse_case("wORLD") == "World"

def test_convert_to_inverse_case_with_numbers_and_symbols():
    assert convert_to_inverse_case("Hello123!") == "hELLO123!"
    assert convert_to_inverse_case("PyThOn!") == "pYtHoN!"

def test_convert_to_inverse_case_empty_string():
    assert convert_to_inverse_case("") == ""

def test_convert_to_inverse_case_all_cases():
    assert convert_to_inverse_case("AbCdEfG123!@#") == "aBcDeFg123!@#"

def test_convert_to_inverse_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_inverse_case(123)
    with pytest.raises(TypeError):
        convert_to_inverse_case(None)