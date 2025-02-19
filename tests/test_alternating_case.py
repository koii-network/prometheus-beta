import pytest
from src.alternating_case import alternating_sentence_case

def test_alternating_sentence_case_basic():
    """Test basic alternating case conversion."""
    assert alternating_sentence_case("hello world") == "HeLlO WoRlD"

def test_alternating_sentence_case_empty_string():
    """Test empty string input."""
    assert alternating_sentence_case("") == ""

def test_alternating_sentence_case_single_char():
    """Test single character input."""
    assert alternating_sentence_case("a") == "A"

def test_alternating_sentence_case_with_spaces():
    """Test string with multiple spaces."""
    assert alternating_sentence_case("  test  string  ") == "  TeSt  StRiNg  "

def test_alternating_sentence_case_mixed_case():
    """Test string with mixed case input."""
    assert alternating_sentence_case("MiXeD cAsE") == "MiXeD CaSe"

def test_alternating_sentence_case_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        alternating_sentence_case(123)
    with pytest.raises(TypeError):
        alternating_sentence_case(None)