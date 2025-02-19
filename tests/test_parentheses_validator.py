import pytest
from src.parentheses_validator import is_valid_parentheses

def test_empty_string():
    assert is_valid_parentheses("") == True

def test_single_valid_pair():
    assert is_valid_parentheses("()") == True

def test_multiple_valid_pairs():
    assert is_valid_parentheses("()()") == True
    assert is_valid_parentheses("(())") == True
    assert is_valid_parentheses("((()))") == True

def test_nested_valid_pairs():
    assert is_valid_parentheses("(()())") == True

def test_invalid_unbalanced_pairs():
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses(")") == False
    assert is_valid_parentheses("(()") == False
    assert is_valid_parentheses("())") == False

def test_invalid_order():
    assert is_valid_parentheses(")(") == False
    assert is_valid_parentheses(")()") == False
    assert is_valid_parentheses("()()(()") == False