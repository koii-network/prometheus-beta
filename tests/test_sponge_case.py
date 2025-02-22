import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic string conversion to sponge case."""
    assert to_sponge_case("hello") == "HeLlO"
    assert to_sponge_case("world") == "WoRlD"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_mixed_case_input():
    """Test conversion of strings with mixed case."""
    assert to_sponge_case("PytHOn") == "PyThOn"

def test_special_characters():
    """Test conversion with special characters and spaces."""
    assert to_sponge_case("hello world!") == "HeLlO WoRlD!"

def test_non_string_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    
    with pytest.raises(TypeError):
        to_sponge_case(None)