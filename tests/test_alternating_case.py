import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case():
    # Test basic functionality
    assert convert_to_alternating_case("hello") == "HeLlO"
    assert convert_to_alternating_case("python") == "PyThOn"
    
    # Test empty string
    assert convert_to_alternating_case("") == ""
    
    # Test string with spaces
    assert convert_to_alternating_case("hello world") == "HeLlO wOrLd"
    
    # Test string with mixed case
    assert convert_to_alternating_case("MiXeD cAsE") == "MiXeD cAsE"
    
    # Test string with special characters
    assert convert_to_alternating_case("hello123!") == "HeLlO123!"
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_alternating_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_case(None)