import pytest
from src.parentheses_validator import is_valid_parentheses

def test_basic_valid_parentheses():
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("(())") == True
    assert is_valid_parentheses("(()())") == True

def test_basic_invalid_parentheses():
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses(")") == False
    assert is_valid_parentheses(")(") == False
    assert is_valid_parentheses("(()") == False

def test_empty_string():
    assert is_valid_parentheses("") == True

def test_nested_parentheses():
    assert is_valid_parentheses("((()))") == True
    assert is_valid_parentheses("((()()))") == True

def test_long_sequences():
    assert is_valid_parentheses("()" * 100) == True
    assert is_valid_parentheses("(" * 50 + ")" * 50) == True

def test_mismatched_parentheses():
    assert is_valid_parentheses("((()") == False
    assert is_valid_parentheses("())") == False
    assert is_valid_parentheses("(()()))(") == False