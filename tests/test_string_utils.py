import pytest
from src.string_utils import to_alternating_case

def test_basic_alternating_case():
    """Test basic alternating case conversion."""
    assert to_alternating_case("hello") == "HeLlO"
    assert to_alternating_case("world") == "WoRlD"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_alternating_case("a") == "A"
    assert to_alternating_case("B") == "B"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert to_alternating_case("hello world") == "HeLlO WoRlD"

def test_mixed_case_input():
    """Test input with mixed existing case."""
    assert to_alternating_case("HeLLo") == "HeLlO"

def test_non_alphabetic_characters():
    """Test input with non-alphabetic characters."""
    assert to_alternating_case("hello123") == "HeLlO123"
    assert to_alternating_case("!@#") == "!@#"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_alternating_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_case(None)
    
    with pytest.raises(TypeError):
        to_alternating_case(["hello"])