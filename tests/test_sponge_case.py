import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic string conversion to sponge case."""
    assert to_sponge_case("hello world") == "hElLo WoRlD"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_sponge_case("a") == "A"
    assert to_sponge_case("B") == "b"

def test_special_characters():
    """Test conversion with special characters and spaces."""
    assert to_sponge_case("hello, world!") == "hElLo, WoRlD!"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_sponge_case("PyThOn") == "pYtHoN"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(None)

def test_unicode_characters():
    """Test conversion with unicode characters."""
    assert to_sponge_case("こんにちは") == "こＮにＣは"