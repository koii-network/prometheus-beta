import pytest
from src.title_case import convert_to_title_case

def test_basic_title_case():
    """Test basic title case conversion."""
    assert convert_to_title_case("hello world") == "Hello World"

def test_already_title_case():
    """Test string that is already in title case."""
    assert convert_to_title_case("Hello World") == "Hello World"

def test_uppercase_input():
    """Test converting uppercase input to title case."""
    assert convert_to_title_case("PYTHON PROGRAMMING") == "Python Programming"

def test_mixed_case_input():
    """Test converting mixed case input to title case."""
    assert convert_to_title_case("pYtHoN pRoGrAmMiNg") == "Python Programming"

def test_empty_string():
    """Test empty string input."""
    assert convert_to_title_case("") == ""

def test_single_word():
    """Test single word input."""
    assert convert_to_title_case("python") == "Python"

def test_multiple_spaces():
    """Test input with multiple spaces."""
    assert convert_to_title_case("  hello   world  ") == "Hello World"

def test_input_with_hyphens():
    """Test input with hyphens."""
    assert convert_to_title_case("python-programming language") == "Python-Programming Language"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(None)