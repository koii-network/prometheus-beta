import pytest
from src.alternating_caps import to_alternating_caps

def test_basic_alternating_caps():
    """Test basic string conversion to alternating caps."""
    assert to_alternating_caps("hello") == "HeLlO"
    assert to_alternating_caps("world") == "WoRlD"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_caps("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_alternating_caps("a") == "A"
    assert to_alternating_caps("b") == "B"

def test_mixed_case_input():
    """Test input with mixed existing case."""
    assert to_alternating_caps("AbCdEf") == "AbCdEf"

def test_spaces_and_special_characters():
    """Test string with spaces and special characters."""
    assert to_alternating_caps("hello world!") == "HeLlO WoRlD!"

def test_non_string_input():
    """Test raising TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        to_alternating_caps(123)
    
    with pytest.raises(TypeError):
        to_alternating_caps(None)
    
    with pytest.raises(TypeError):
        to_alternating_caps(["list"])