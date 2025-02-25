import pytest
from src.sentence_case import convert_to_sentence_case

def test_convert_to_sentence_case_normal_input():
    """Test conversion of normal mixed-case string."""
    assert convert_to_sentence_case("HELLO WORLD") == "Hello world"
    assert convert_to_sentence_case("hello WORLD") == "Hello world"
    assert convert_to_sentence_case("Hello World") == "Hello world"

def test_convert_to_sentence_case_edge_cases():
    """Test edge cases for sentence case conversion."""
    # Empty string
    assert convert_to_sentence_case("") == ""
    
    # Single character
    assert convert_to_sentence_case("a") == "A"
    assert convert_to_sentence_case("Z") == "Z"
    
    # String with only whitespace
    assert convert_to_sentence_case("   ") == "   "

def test_convert_to_sentence_case_error_handling():
    """Test error handling for invalid inputs."""
    # Non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_sentence_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_sentence_case(None)

def test_convert_to_sentence_case_whitespace():
    """Test handling of strings with whitespace."""
    assert convert_to_sentence_case("  hello world  ") == "  Hello world  "
    assert convert_to_sentence_case(" HELLO ") == " Hello "

def test_convert_to_sentence_case_special_characters():
    """Test handling of strings with special characters."""
    assert convert_to_sentence_case("hello, world!") == "Hello, world!"
    assert convert_to_sentence_case("123 abc") == "123 abc"