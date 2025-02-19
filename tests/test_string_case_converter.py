import pytest
from src.string_case_converter import convert_to_sentence_case

def test_convert_to_sentence_case():
    # Test normal strings
    assert convert_to_sentence_case("hello world") == "Hello world"
    assert convert_to_sentence_case("HELLO WORLD") == "Hello world"
    assert convert_to_sentence_case("hello WORLD") == "Hello world"
    
    # Test strings with different capitalizations
    assert convert_to_sentence_case("hELLO wORLD") == "Hello world"
    
    # Test single character strings
    assert convert_to_sentence_case("a") == "A"
    assert convert_to_sentence_case("Z") == "Z"
    
    # Test empty string
    assert convert_to_sentence_case("") == ""
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_sentence_case(None)
    with pytest.raises(TypeError):
        convert_to_sentence_case(123)
    with pytest.raises(TypeError):
        convert_to_sentence_case(["hello"])