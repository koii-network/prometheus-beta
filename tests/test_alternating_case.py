import pytest
from src.alternating_case import to_alternating_case

def test_to_alternating_case_basic():
    """Test basic string conversion to alternating case."""
    assert to_alternating_case("hello") == "HeLlO"
    assert to_alternating_case("world") == "WoRlD"

def test_to_alternating_case_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_case("") == ""

def test_to_alternating_case_mixed_case():
    """Test conversion of mixed case strings."""
    assert to_alternating_case("HeLLo") == "HeLlO"
    assert to_alternating_case("WoRlD") == "WoRlD"

def test_to_alternating_case_with_spaces():
    """Test conversion of strings with spaces."""
    assert to_alternating_case("hello world") == "HeLlO WoRlD"

def test_to_alternating_case_with_numbers_and_symbols():
    """Test conversion of strings with numbers and symbols."""
    assert to_alternating_case("hello123 world!") == "HeLlO123 WoRlD!"

def test_to_alternating_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_case(["hello"])