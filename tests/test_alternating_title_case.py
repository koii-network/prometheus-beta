import pytest
from src.alternating_title_case import alternating_title_case

def test_alternating_title_case_basic():
    """Test basic alternating title case conversion."""
    assert alternating_title_case("hello world python") == "Hello world Python"

def test_alternating_title_case_multiple_words():
    """Test alternating title case with multiple words."""
    assert alternating_title_case("the quick brown fox jumps") == "The quick Brown fox Jumps"

def test_alternating_title_case_single_word():
    """Test alternating title case with a single word."""
    assert alternating_title_case("hello") == "Hello"

def test_alternating_title_case_empty_string():
    """Test alternating title case with an empty string."""
    assert alternating_title_case("") == ""

def test_alternating_title_case_type_error():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        alternating_title_case(123)

def test_alternating_title_case_mixed_case():
    """Test alternating title case with mixed case input."""
    assert alternating_title_case("HELLO world PYTHON programming") == "Hello world Python programming"