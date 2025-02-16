import pytest
from src.string_utils import convert_to_inverse_case

def test_convert_to_inverse_case_basic():
    assert convert_to_inverse_case("Hello World") == "hELLO wORLD"
    assert convert_to_inverse_case("PYTHON") == "python"
    assert convert_to_inverse_case("python") == "PYTHON"

def test_convert_to_inverse_case_empty_string():
    assert convert_to_inverse_case("") == ""

def test_convert_to_inverse_case_mixed_chars():
    assert convert_to_inverse_case("HeLLo 123 WoRlD!") == "hEllO 123 wOrLd!"

def test_convert_to_inverse_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_inverse_case(123)
    with pytest.raises(TypeError):
        convert_to_inverse_case(None)