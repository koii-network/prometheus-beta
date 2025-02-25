import pytest
from src.string_case_converter import convert_to_alternating_pascal_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert convert_to_alternating_pascal_case("hello world") == "HeLlO WoRlD"
    assert convert_to_alternating_pascal_case("python programming") == "PyThOn PrOgRaMmInG"

def test_single_word():
    """Test conversion of a single word"""
    assert convert_to_alternating_pascal_case("python") == "PyThOn"

def test_mixed_case_input():
    """Test input with mixed case"""
    assert convert_to_alternating_pascal_case("HeLLo WoRlD") == "HeLlO WoRlD"

def test_multiple_spaces():
    """Test input with multiple spaces"""
    assert convert_to_alternating_pascal_case("hello   world") == "HeLlO WoRlD"

def test_edge_cases():
    """Test edge cases"""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_pascal_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_pascal_case(None)
    
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_alternating_pascal_case("")

def test_special_characters():
    """Test conversion with special characters"""
    assert convert_to_alternating_pascal_case("hello! world") == "HeLlO! WoRlD"
    assert convert_to_alternating_pascal_case("python-programming") == "PyThOn-pRoGrAmMiNg"