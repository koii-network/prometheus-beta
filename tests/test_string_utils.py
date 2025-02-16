import pytest
from src.string_utils import to_lowercase

def test_to_lowercase_basic():
    """Test basic lowercase conversion."""
    assert to_lowercase("HELLO") == "hello"
    assert to_lowercase("World") == "world"
    assert to_lowercase("python") == "python"

def test_to_lowercase_empty_string():
    """Test lowercase conversion with an empty string."""
    assert to_lowercase("") == ""

def test_to_lowercase_mixed_case():
    """Test lowercase conversion with mixed case string."""
    assert to_lowercase("HeLLo WoRLD") == "hello world"

def test_to_lowercase_with_numbers_and_symbols():
    """Test lowercase conversion with numbers and symbols."""
    assert to_lowercase("Hello123!@#") == "hello123!@#"

def test_to_lowercase_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_lowercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_lowercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_lowercase(["list"])