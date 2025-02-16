import pytest
from src.alternating_title_case import alternating_title_case

def test_alternating_title_case_basic():
    """Test basic functionality of alternating title case."""
    assert alternating_title_case("hello world python") == "HELLO world PYTHON"

def test_alternating_title_case_single_word():
    """Test single word input."""
    assert alternating_title_case("hello") == "HELLO"

def test_alternating_title_case_empty_string():
    """Test empty string input."""
    assert alternating_title_case("") == ""

def test_alternating_title_case_multiple_words():
    """Test multiple words with alternating case."""
    assert alternating_title_case("one two three four five") == "ONE two THREE four FIVE"

def test_alternating_title_case_error_non_string():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        alternating_title_case(123)
        
def test_alternating_title_case_with_extra_spaces():
    """Test input with extra spaces."""
    assert alternating_title_case("  hello   world  ") == "HELLO world"