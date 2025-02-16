import pytest
from src.sponge_case import convert_to_sponge_case

def test_convert_to_sponge_case():
    # Test basic conversion
    assert convert_to_sponge_case("hello") == "HeLlO"
    
    # Test empty string
    assert convert_to_sponge_case("") == ""
    
    # Test string with spaces and mixed case
    assert convert_to_sponge_case("python is fun") == "PyThOn Is FuN"
    
    # Test string with special characters
    assert convert_to_sponge_case("hello, world!") == "HeLlO, WoRlD!"
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_sponge_case(123)
    
    with pytest.raises(TypeError):
        convert_to_sponge_case(None)