import pytest
from src.string_case_converter import convert_to_sentence_case

def test_convert_to_sentence_case_normal():
    """Test conversion of a normal string."""
    assert convert_to_sentence_case("HELLO WORLD") == "Hello world"
    assert convert_to_sentence_case("hello WORLD") == "Hello world"

def test_convert_to_sentence_case_empty():
    """Test conversion of an empty string."""
    assert convert_to_sentence_case("") == ""

def test_convert_to_sentence_case_single_char():
    """Test conversion of a single character."""
    assert convert_to_sentence_case("a") == "A"
    assert convert_to_sentence_case("Z") == "Z"

def test_convert_to_sentence_case_mixed_case():
    """Test conversion of mixed case string."""
    assert convert_to_sentence_case("hElLo WoRlD") == "Hello world"

def test_convert_to_sentence_case_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError):
        convert_to_sentence_case(123)
    with pytest.raises(TypeError):
        convert_to_sentence_case(None)