import pytest
from src.parentheses_validator import validate_parentheses

def test_balanced_parentheses():
    # Test simple balanced cases
    assert validate_parentheses("()") == True
    assert validate_parentheses("(())") == True
    assert validate_parentheses("()()") == True

def test_unbalanced_parentheses():
    # Test various unbalanced cases
    assert validate_parentheses("(") == False
    assert validate_parentheses(")") == False
    assert validate_parentheses(")(") == False
    assert validate_parentheses("((") == False
    assert validate_parentheses("))") == False

def test_empty_string():
    # Empty string is considered balanced
    assert validate_parentheses("") == True

def test_complex_balanced_cases():
    # More complex balanced cases
    assert validate_parentheses("(()())") == True
    assert validate_parentheses("((()))") == True

def test_complex_unbalanced_cases():
    # More complex unbalanced cases
    assert validate_parentheses("(()") == False
    assert validate_parentheses("())") == False
    assert validate_parentheses("((()") == False