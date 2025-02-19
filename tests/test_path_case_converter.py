import pytest
from src.path_case_converter import convert_to_path_case

def test_convert_to_path_case():
    # Test basic conversion
    assert convert_to_path_case("Hello World") == "hello-world"
    
    # Test with multiple spaces
    assert convert_to_path_case("Hello   World") == "hello-world"
    
    # Test with underscores
    assert convert_to_path_case("Hello_World") == "hello-world"
    
    # Test with mixed spaces and underscores
    assert convert_to_path_case("Hello World_Test") == "hello-world-test"
    
    # Test with leading and trailing spaces
    assert convert_to_path_case("  Hello World  ") == "hello-world"
    
    # Test with already lowercase string
    assert convert_to_path_case("hello-world") == "hello-world"
    
    # Test empty string
    assert convert_to_path_case("") == ""

def test_convert_to_path_case_error_handling():
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_path_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_path_case(None)