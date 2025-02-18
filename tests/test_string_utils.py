import pytest
from src.string_utils import to_uppercase

def test_to_uppercase_basic():
    """Test basic uppercase conversion."""
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("world") == "WORLD"

def test_to_uppercase_mixed_case():
    """Test uppercase conversion for mixed case strings."""
    assert to_uppercase("HeLLo WoRLd") == "HELLO WORLD"

def test_to_uppercase_empty_string():
    """Test uppercase conversion for an empty string."""
    assert to_uppercase("") == ""

def test_to_uppercase_with_numbers_and_symbols():
    """Test uppercase conversion with numbers and symbols."""
    assert to_uppercase("hello123!@#") == "HELLO123!@#"

def test_to_uppercase_non_string_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_uppercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_uppercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_uppercase(["hello"])