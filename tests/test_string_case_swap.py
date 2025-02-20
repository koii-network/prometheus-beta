import pytest
from src.string_case_swap import swap_case

def test_swap_case_mixed_string():
    """Test swapping case in a mixed case string"""
    assert swap_case("Hello World") == "hELLO wORLD"

def test_swap_case_uppercase():
    """Test swapping case in an uppercase string"""
    assert swap_case("PYTHON") == "python"

def test_swap_case_lowercase():
    """Test swapping case in a lowercase string"""
    assert swap_case("programming") == "PROGRAMMING"

def test_swap_case_empty_string():
    """Test swapping case in an empty string"""
    assert swap_case("") == ""

def test_swap_case_with_numbers_and_symbols():
    """Test swapping case with numbers and symbols"""
    assert swap_case("Hello123!@#") == "hELLO123!@#"