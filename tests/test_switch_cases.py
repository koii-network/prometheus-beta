import pytest
from src.switch_cases import switch_cases

def test_switch_cases_basic():
    """Test basic case swapping."""
    result = switch_cases("Hello", "World")
    assert result == "hELLO"

def test_switch_cases_mixed_case():
    """Test case swapping with mixed case input."""
    result = switch_cases("HeLLo", "World")
    assert result == "hEllO"

def test_switch_cases_empty_string():
    """Test with an empty first string."""
    result = switch_cases("", "World")
    assert result == ""

def test_switch_cases_all_uppercase():
    """Test case swapping with all uppercase input."""
    result = switch_cases("HELLO", "World")
    assert result == "hello"

def test_switch_cases_all_lowercase():
    """Test case swapping with all lowercase input."""
    result = switch_cases("hello", "World")
    assert result == "HELLO"

def test_switch_cases_with_numbers_and_symbols():
    """Test case swapping with numbers and symbols."""
    result = switch_cases("Hello123!", "World")
    assert result == "hELLO123!"