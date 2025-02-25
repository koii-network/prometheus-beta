import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic string conversion to sponge case."""
    assert to_sponge_case("hello") == "hElLo"
    assert to_sponge_case("python") == "pYtHoN"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_sponge_case("a") == "a"
    assert to_sponge_case("B") == "b"

def test_mixed_case_input():
    """Test conversion of input with mixed case."""
    assert to_sponge_case("HeLLo") == "hElLo"

def test_string_with_spaces():
    """Test conversion of string with spaces."""
    assert to_sponge_case("hello world") == "hElLo wOrLd"

def test_string_with_symbols():
    """Test conversion of string with symbols."""
    assert to_sponge_case("hello, world!") == "hElLo, wOrLd!"

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(None)