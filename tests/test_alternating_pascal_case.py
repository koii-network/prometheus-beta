import pytest
from src.alternating_pascal_case import convert_to_alternating_pascal_case

def test_convert_to_alternating_pascal_case():
    # Test various input scenarios
    assert convert_to_alternating_pascal_case("hello world") == "HelloWorld"
    assert convert_to_alternating_pascal_case("python is awesome") == "PythonIsAwesome"
    assert convert_to_alternating_pascal_case("a b c d") == "ABCd"
    
    # Test with special characters
    assert convert_to_alternating_pascal_case("hello, world!") == "HelloWorld"
    assert convert_to_alternating_pascal_case("python 2.0 rocks") == "Python2Rocks"
    
    # Test edge cases
    assert convert_to_alternating_pascal_case("") == ""
    assert convert_to_alternating_pascal_case("single") == "Single"
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(None)
    
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(123)

def test_alternating_case_pattern():
    # Additional tests to verify alternating case pattern
    assert convert_to_alternating_pascal_case("one two three four") == "OneTwoThreeFour"
    assert convert_to_alternating_pascal_case("red green blue yellow") == "RedGreenBlueYellow"