import pytest
from src.alternating_caps import to_alternating_caps

def test_alternating_caps_basic():
    """Test basic string conversion"""
    assert to_alternating_caps("hello") == "HeLlO"
    assert to_alternating_caps("world") == "WoRlD"

def test_alternating_caps_mixed_case():
    """Test strings with mixed initial case"""
    assert to_alternating_caps("pYtHoN") == "PyThOn"

def test_alternating_caps_empty_string():
    """Test empty string handling"""
    assert to_alternating_caps("") == ""

def test_alternating_caps_single_character():
    """Test single character string"""
    assert to_alternating_caps("a") == "A"
    assert to_alternating_caps("Z") == "Z"

def test_alternating_caps_with_spaces():
    """Test string with spaces"""
    assert to_alternating_caps("hello world") == "HeLlO WoRlD"

def test_alternating_caps_with_punctuation():
    """Test string with punctuation"""
    assert to_alternating_caps("hello, world!") == "HeLlO, WoRlD!"

def test_alternating_caps_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        to_alternating_caps(None)
    with pytest.raises(TypeError):
        to_alternating_caps(123)
    with pytest.raises(TypeError):
        to_alternating_caps(["list"])