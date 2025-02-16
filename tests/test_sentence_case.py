import pytest
from src.sentence_case import convert_to_sentence_case

def test_convert_to_sentence_case_basic():
    """Test basic sentence case conversion."""
    assert convert_to_sentence_case("hello world") == "Hello world"
    assert convert_to_sentence_case("HELLO WORLD") == "Hello world"
    assert convert_to_sentence_case("hELLO wORLD") == "Hello world"

def test_convert_to_sentence_case_edge_cases():
    """Test edge cases for sentence case conversion."""
    assert convert_to_sentence_case("") == ""
    assert convert_to_sentence_case("a") == "A"
    assert convert_to_sentence_case("A") == "A"

def test_convert_to_sentence_case_invalid_input():
    """Test that invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        convert_to_sentence_case(123)
    with pytest.raises(TypeError):
        convert_to_sentence_case(None)