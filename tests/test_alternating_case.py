import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    """Test basic alternating case conversion."""
    assert convert_to_alternating_case("hello") == "HeLlO"
    assert convert_to_alternating_case("world") == "WoRlD"

def test_convert_to_alternating_case_multiple_words():
    """Test alternating case with multiple words."""
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"

def test_convert_to_alternating_case_mixed_case():
    """Test alternating case with mixed input."""
    assert convert_to_alternating_case("PytHoN pRoGrAmMiNg") == "PyThOn PrOgRaMmInG"

def test_convert_to_alternating_case_symbols_and_numbers():
    """Test alternating case with symbols and numbers."""
    assert convert_to_alternating_case("hello 123 world!") == "HeLlO 123 WoRlD!"

def test_convert_to_alternating_case_empty_string():
    """Test that empty string raises ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_alternating_case("")

def test_convert_to_alternating_case_non_string():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(None)