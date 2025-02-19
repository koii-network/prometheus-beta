import pytest
from src.validate_parentheses import is_valid_parentheses

def test_valid_parentheses():
    # Basic valid cases
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()()") == True
    assert is_valid_parentheses("(())") == True
    
def test_invalid_parentheses():
    # Basic invalid cases
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses(")") == False
    assert is_valid_parentheses(")(") == False
    assert is_valid_parentheses("())") == False
    
def test_empty_string():
    # Empty string is considered valid
    assert is_valid_parentheses("") == True
    
def test_complex_cases():
    # More complex valid and invalid cases
    assert is_valid_parentheses("((()))") == True
    assert is_valid_parentheses("(()())") == True
    assert is_valid_parentheses("((()())())") == True
    assert is_valid_parentheses("((()") == False
    assert is_valid_parentheses("(())(") == False

def test_other_characters():
    # Function does not handle non-parenthesis characters
    with pytest.raises(TypeError):
        is_valid_parentheses("(a)")