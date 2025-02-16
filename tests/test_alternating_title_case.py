import pytest
from src.alternating_title_case import alternating_title_case

def test_alternating_title_case_basic():
    """Test basic alternating title case conversion."""
    assert alternating_title_case("hello world python") == "Hello world Python"

def test_alternating_title_case_multiple_words():
    """Test conversion with multiple words."""
    assert alternating_title_case("this is a test string") == "This is A test String"

def test_alternating_title_case_empty_string():
    """Test with an empty string."""
    assert alternating_title_case("") == ""

def test_alternating_title_case_single_word():
    """Test with a single word."""
    assert alternating_title_case("hello") == "Hello"

def test_alternating_title_case_error_non_string():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        alternating_title_case(123)

def test_alternating_title_case_with_existing_mixed_case():
    """Test conversion with words that already have mixed case."""
    assert alternating_title_case("HELLO world PYTHON test") == "Hello world Python test"