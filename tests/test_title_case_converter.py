import pytest
from src.title_case_converter import convert_to_title_case

def test_basic_conversion():
    """Test basic string to title case conversion."""
    assert convert_to_title_case("hello world") == "Hello World"

def test_uppercase_input():
    """Test conversion of uppercase string."""
    assert convert_to_title_case("PYTHON PROGRAMMING") == "Python Programming"

def test_mixed_case_input():
    """Test conversion of mixed case string."""
    assert convert_to_title_case("openAI chatGPT") == "Openai Chatgpt"

def test_single_word():
    """Test conversion of a single word."""
    assert convert_to_title_case("python") == "Python"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_title_case("") == ""

def test_string_with_multiple_spaces():
    """Test conversion of string with multiple spaces."""
    assert convert_to_title_case("  hello   world  ") == "Hello World"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(None)

def test_string_with_special_characters():
    """Test conversion of string with special characters."""
    assert convert_to_title_case("hello, world! how are you?") == "Hello, World! How Are You?"