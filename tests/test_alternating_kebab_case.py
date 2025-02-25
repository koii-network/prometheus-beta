import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_alternating_kebab_case_basic():
    # Basic conversion test
    assert to_alternating_kebab_case("hello world") == "hello-WORLD"
    
def test_alternating_kebab_case_multiple_words():
    # Multiple words test
    assert to_alternating_kebab_case("hello beautiful world") == "hello-BEAUTIFUL-world"
    
def test_alternating_kebab_case_with_punctuation():
    # Test with punctuation and special characters
    assert to_alternating_kebab_case("hello, beautiful world!") == "hello-BEAUTIFUL-world"
    
def test_alternating_kebab_case_empty_string():
    # Empty string test
    assert to_alternating_kebab_case("") == ""
    
def test_alternating_kebab_case_single_word():
    # Single word test
    assert to_alternating_kebab_case("hello") == "hello"
    
def test_alternating_kebab_case_mixed_case():
    # Mixed case input test
    assert to_alternating_kebab_case("Hello BEAUTIFUL World") == "hello-BEAUTIFUL-world"
    
def test_alternating_kebab_case_invalid_input():
    # Invalid input type test
    with pytest.raises(TypeError):
        to_alternating_kebab_case(123)
        
def test_alternating_kebab_case_with_numbers():
    # Test with numbers
    assert to_alternating_kebab_case("hello 123 world") == "hello-123-WORLD"