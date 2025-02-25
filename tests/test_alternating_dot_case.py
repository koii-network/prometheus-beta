import pytest
from src.alternating_dot_case import to_alternating_dot_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert to_alternating_dot_case("hello world") == "hElLo.WoRlD"

def test_mixed_case_input():
    """Test input with mixed case"""
    assert to_alternating_dot_case("PYTHON programming") == "pYtHoN.PrOgRaMmInG"

def test_empty_string():
    """Test empty string input"""
    assert to_alternating_dot_case("") == ""

def test_single_character():
    """Test single character input"""
    assert to_alternating_dot_case("a") == "a"

def test_non_alphabetic_characters():
    """Test input with numbers and special characters"""
    assert to_alternating_dot_case("hello123 world!") == "hElLoNeXtCNeXtCNeXtC.WoRlD."

def test_input_type_error():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError):
        to_alternating_dot_case(123)
    with pytest.raises(TypeError):
        to_alternating_dot_case(None)

def test_unicode_characters():
    """Test input with unicode characters"""
    assert to_alternating_dot_case("こんにちは") == "こんにちは"