import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    """Test basic string conversion"""
    assert convert_to_alternating_case("hello world") == "HeLlO wOrLd"
    assert convert_to_alternating_case("PYTHON PROGRAMMING") == "PyThOn PrOgRaMmInG"

def test_convert_to_alternating_case_empty_string():
    """Test empty string input"""
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_single_char():
    """Test single character input"""
    assert convert_to_alternating_case("a") == "A"
    assert convert_to_alternating_case("Z") == "Z"

def test_convert_to_alternating_case_with_special_chars():
    """Test string with special characters and spaces"""
    assert convert_to_alternating_case("hello, world! 123") == "HeLlO, WoRlD! 123"

def test_convert_to_alternating_case_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        convert_to_alternating_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_case(None)

def test_convert_to_alternating_case_unicode():
    """Test conversion with unicode characters"""
    assert convert_to_alternating_case("résumé") == "RéSuMé"