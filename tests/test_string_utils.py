import pytest
from src.string_utils import switch_cases

def test_switch_cases_basic():
    """Test basic case switching"""
    assert switch_cases("hello", "WORLD") == "HELLO"
    assert switch_cases("HELLO", "world") == "hello"

def test_switch_cases_mixed():
    """Test mixed case scenarios"""
    assert switch_cases("hElLo", "WoRlD") == "HeLLo"
    assert switch_cases("PyThOn", "jAvAsCrIpT") == "PYthON"

def test_switch_cases_equal_length():
    """Test that input strings must be of equal length"""
    with pytest.raises(ValueError):
        switch_cases("short", "longer")

def test_switch_cases_type_validation():
    """Test type validation of inputs"""
    with pytest.raises(TypeError):
        switch_cases(123, "abc")
    with pytest.raises(TypeError):
        switch_cases("abc", None)

def test_switch_cases_empty_string():
    """Test with empty strings"""
    assert switch_cases("", "") == ""