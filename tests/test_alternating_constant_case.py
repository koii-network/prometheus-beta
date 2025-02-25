import pytest
from src.alternating_constant_case import convert_to_alternating_constant_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert convert_to_alternating_constant_case("hello world") == "HELLO world"
    assert convert_to_alternating_constant_case("python is awesome") == "PYTHON is AWESOME"

def test_single_word():
    """Test conversion with a single word"""
    assert convert_to_alternating_constant_case("hello") == "HELLO"

def test_multiple_words():
    """Test conversion with multiple words"""
    assert convert_to_alternating_constant_case("one two three four") == "ONE two THREE four"

def test_already_uppercase():
    """Test conversion with already uppercase words"""
    assert convert_to_alternating_constant_case("HELLO world") == "HELLO world"

def test_mixed_case():
    """Test conversion with mixed case words"""
    assert convert_to_alternating_constant_case("HeLLo WoRlD") == "HELLO world"

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_constant_case(123)
    
    # Test empty string
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_alternating_constant_case("")

def test_whitespace_handling():
    """Test handling of multiple whitespaces"""
    assert convert_to_alternating_constant_case("   hello   world   ") == "HELLO world"