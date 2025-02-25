import pytest
from src.switch_cases import switch_cases

def test_switch_cases_basic():
    """Test basic functionality of switching cases"""
    assert switch_cases("Hello", "World") == "hELLOwORLD"

def test_switch_cases_mixed_strings():
    """Test with mixed case strings"""
    assert switch_cases("HeLLo", "wOrLd") == "hEllOWOrLd"

def test_switch_cases_empty_strings():
    """Test with empty strings"""
    assert switch_cases("", "") == ""

def test_switch_cases_numbers_and_symbols():
    """Test with strings containing numbers and symbols"""
    assert switch_cases("123!", "ABC@") == "123!abc@"

def test_switch_cases_unicode():
    """Test with unicode characters"""
    assert switch_cases("HÃ©llo", "WÃ¶rld") == "hÃLLOwÃRLD"