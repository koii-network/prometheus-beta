import pytest
from src.string_converter import convert_to_constant_case

def test_convert_to_constant_case():
    # Test various input formats
    assert convert_to_constant_case("hello world") == "HELLO_WORLD"
    assert convert_to_constant_case("hello-world") == "HELLO_WORLD"
    assert convert_to_constant_case("helloWorld") == "HELLO_WORLD"
    assert convert_to_constant_case("  hello  world  ") == "HELLO_WORLD"
    
    # Test edge cases
    assert convert_to_constant_case("") == ""
    assert convert_to_constant_case("singleword") == "SINGLEWORD"
    
    # Test with multiple separators
    assert convert_to_constant_case("hello--world") == "HELLO_WORLD"
    assert convert_to_constant_case("hello world test") == "HELLO_WORLD_TEST"
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_constant_case(123)
    
    with pytest.raises(TypeError):
        convert_to_constant_case(None)