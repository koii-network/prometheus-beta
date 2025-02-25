import pytest
from src.alternating_snake_case import to_alternating_snake_case

def test_basic_string_conversion():
    """Test basic string conversion to alternating snake case."""
    assert to_alternating_snake_case("hello world") == 'hElLo_wOrLd'
    assert to_alternating_snake_case("Python Programming") == 'pYtHoN_pRoGrAmMiNg'

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_snake_case("python") == 'pYtHoN'

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_snake_case("") == ""

def test_string_with_existing_snake_case():
    """Test conversion of a string with existing snake case."""
    assert to_alternating_snake_case("hello_world") == 'hElLo_wOrLd'

def test_mixed_case_input():
    """Test conversion of mixed case input."""
    assert to_alternating_snake_case("HeLLo WoRLd") == 'hElLo_wOrLd'

def test_input_with_special_characters():
    """Test conversion of input with special characters."""
    assert to_alternating_snake_case("hello world!") == 'hElLo_wOrLd!'

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_snake_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_snake_case(None)