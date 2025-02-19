import pytest
from src.string_converter import convert_to_sentence_case

def test_convert_to_sentence_case_normal():
    """Test converting a normal string to sentence case."""
    assert convert_to_sentence_case("HELLO WORLD") == "Hello world"
    assert convert_to_sentence_case("hello WORLD") == "Hello world"

def test_convert_to_sentence_case_empty():
    """Test converting an empty string."""
    assert convert_to_sentence_case("") == ""

def test_convert_to_sentence_case_single_word():
    """Test converting a single word."""
    assert convert_to_sentence_case("HELLO") == "Hello"
    assert convert_to_sentence_case("hello") == "Hello"

def test_convert_to_sentence_case_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        convert_to_sentence_case(123)
    with pytest.raises(TypeError):
        convert_to_sentence_case(None)

def test_convert_to_sentence_case_mixed_case():
    """Test converting strings with mixed case."""
    assert convert_to_sentence_case("hElLo WoRlD") == "Hello world"