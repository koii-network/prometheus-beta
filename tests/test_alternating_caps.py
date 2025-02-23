import pytest
from src.alternating_caps import to_alternating_caps

def test_basic_alternating_caps():
    """Test basic string conversion to alternating caps."""
    assert to_alternating_caps("hello") == "HeLlO"
    assert to_alternating_caps("python") == "PyThOn"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_caps("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_alternating_caps("a") == "A"
    assert to_alternating_caps("B") == "B"

def test_numbers_and_symbols():
    """Test conversion of strings with numbers and symbols."""
    assert to_alternating_caps("123") == "123"
    assert to_alternating_caps("a1b2c3") == "A1b2C3"
    assert to_alternating_caps("!@#") == "!@#"

def test_mixed_case_input():
    """Test conversion of strings with mixed case input."""
    assert to_alternating_caps("MiXeD") == "MiXeD"

def test_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_caps(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_caps(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_caps(["hello"])