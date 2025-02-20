import pytest
from src.case_swap import swap_case

def test_swap_case_normal_string():
    """Test swapping case in a normal mixed-case string"""
    assert swap_case("Hello World") == "hELLO wORLD"

def test_swap_case_all_lowercase():
    """Test swapping case for an all-lowercase string"""
    assert swap_case("hello") == "HELLO"

def test_swap_case_all_uppercase():
    """Test swapping case for an all-uppercase string"""
    assert swap_case("WORLD") == "world"

def test_swap_case_with_numbers_and_symbols():
    """Test swapping case with numbers and symbols present"""
    assert swap_case("Hello123!@#") == "hELLO123!@#"

def test_swap_case_empty_string():
    """Test swapping case for an empty string"""
    assert swap_case("") == ""

def test_swap_case_invalid_input():
    """Test that a TypeError is raised for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        swap_case(123)
        swap_case(None)