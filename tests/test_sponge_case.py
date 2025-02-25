import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic sponge case conversion."""
    assert to_sponge_case("hello world") == "HeLlO wOrLd"

def test_empty_string():
    """Test empty string input."""
    assert to_sponge_case("") == ""

def test_single_character():
    """Test single character input."""
    assert to_sponge_case("a") == "A"
    assert to_sponge_case("B") == "B"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_sponge_case("PyThOn") == "PyThOn"

def test_special_characters():
    """Test input with special characters."""
    assert to_sponge_case("hello, world!") == "HeLlO, wOrLd!"

def test_numeric_input():
    """Test input with numbers."""
    assert to_sponge_case("hello 123") == "HeLlO 123"

def test_invalid_input_type():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(None)
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(["hello"])