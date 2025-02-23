import pytest
from src.case_converter import swap_case

def test_swap_case_normal_string():
    """Test swap_case with a normal mixed-case string."""
    assert swap_case("Hello World!") == "hELLO wORLD!"

def test_swap_case_all_lowercase():
    """Test swap_case with an all-lowercase string."""
    assert swap_case("python") == "PYTHON"

def test_swap_case_all_uppercase():
    """Test swap_case with an all-uppercase string."""
    assert swap_case("PYTHON") == "python"

def test_swap_case_empty_string():
    """Test swap_case with an empty string."""
    assert swap_case("") == ""

def test_swap_case_with_numbers_and_symbols():
    """Test swap_case with numbers and symbols."""
    assert swap_case("Hello123 World!") == "hELLO123 wORLD!"

def test_swap_case_invalid_input():
    """Test swap_case with invalid input type."""
    with pytest.raises(TypeError):
        swap_case(123)
    with pytest.raises(TypeError):
        swap_case(None)