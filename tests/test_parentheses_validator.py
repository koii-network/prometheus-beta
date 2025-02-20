import pytest
from src.parentheses_validator import is_parentheses_nested

def test_simple_matching_parentheses():
    assert is_parentheses_nested("()") == True

def test_nested_parentheses():
    assert is_parentheses_nested("(())") == True

def test_multiple_nested_parentheses():
    assert is_parentheses_nested("(()())") == True

def test_unbalanced_parentheses_extra_opening():
    assert is_parentheses_nested("(()") == False

def test_unbalanced_parentheses_extra_closing():
    assert is_parentheses_nested("())") == False

def test_incorrect_order():
    assert is_parentheses_nested(")(") == False

def test_empty_string():
    assert is_parentheses_nested("") == True

def test_complex_nested_parentheses():
    assert is_parentheses_nested("((()()))") == True

def test_no_parentheses():
    assert is_parentheses_nested("abcde") == True

def test_multiple_unbalanced_nested_parentheses():
    assert is_parentheses_nested("((()") == False