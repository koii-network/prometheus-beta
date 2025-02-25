import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic sponge case conversion."""
    assert to_sponge_case("hello") == "HeLlO"
    assert to_sponge_case("world") == "WoRlD"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_sponge_case("a") == "A"
    assert to_sponge_case("Z") == "Z"

def test_mixed_case_input():
    """Test conversion of strings with mixed case."""
    assert to_sponge_case("HeLLo") == "HeLlO"
    assert to_sponge_case("WoRlD") == "WoRlD"

def test_special_characters():
    """Test conversion with special characters and spaces."""
    assert to_sponge_case("hello world!") == "HeLlO WoRlD!"
    assert to_sponge_case("123 abc") == "123 AbC"

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    with pytest.raises(TypeError):
        to_sponge_case(None)
    with pytest.raises(TypeError):
        to_sponge_case(["list"])