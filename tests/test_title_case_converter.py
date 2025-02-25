import pytest
from src.title_case_converter import convert_to_title_case

def test_basic_conversion():
    """Test basic string to title case conversion."""
    assert convert_to_title_case("hello world") == "Hello World"
    assert convert_to_title_case("python programming") == "Python Programming"

def test_already_title_case():
    """Test that strings already in title case remain unchanged."""
    assert convert_to_title_case("Hello World") == "Hello World"

def test_mixed_case():
    """Test conversion of mixed case strings."""
    assert convert_to_title_case("openAI chatbot") == "Openai Chatbot"
    assert convert_to_title_case("pYtHoN pRoGrAmMiNg") == "Python Programming"

def test_single_word():
    """Test conversion of single words."""
    assert convert_to_title_case("hello") == "Hello"
    assert convert_to_title_case("WORLD") == "World"

def test_empty_string():
    """Test handling of empty string."""
    assert convert_to_title_case("") == ""

def test_whitespace_strings():
    """Test handling of strings with multiple whitespaces."""
    assert convert_to_title_case("  hello   world  ") == "Hello World"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(["hello", "world"])