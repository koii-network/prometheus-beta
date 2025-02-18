import pytest
from src.to_title_case import to_title_case

def test_basic_title_case():
    """Test basic title case conversion."""
    assert to_title_case("hello world") == "Hello World"

def test_single_word():
    """Test single word conversion."""
    assert to_title_case("python") == "Python"

def test_already_title_case():
    """Test string that is already in title case."""
    assert to_title_case("Hello World") == "Hello World"

def test_mixed_case():
    """Test mixed case string conversion."""
    assert to_title_case("hELLo wORLd") == "Hello World"

def test_empty_string():
    """Test empty string conversion."""
    assert to_title_case("") == ""

def test_string_with_multiple_spaces():
    """Test string with multiple spaces."""
    assert to_title_case("  hello   world  ") == "Hello World"

def test_invalid_input_type():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_title_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_title_case(None)