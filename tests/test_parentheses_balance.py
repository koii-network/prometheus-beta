import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_balanced_simple_parentheses():
    assert is_balanced_parentheses("()") == True

def test_balanced_nested_parentheses():
    assert is_balanced_parentheses("((()))") == True

def test_balanced_mixed_parentheses():
    assert is_balanced_parentheses("([{}])") == True

def test_unbalanced_parentheses():
    assert is_balanced_parentheses("(]") == False

def test_unbalanced_extra_closing():
    assert is_balanced_parentheses("())") == False

def test_unbalanced_extra_opening():
    assert is_balanced_parentheses("((()") == False

def test_empty_string():
    assert is_balanced_parentheses("") == True

def test_string_with_no_parentheses():
    assert is_balanced_parentheses("hello world") == True

def test_complex_mixed_case():
    assert is_balanced_parentheses("(hello[world]{test})") == True

def test_complex_unbalanced_mixed_case():
    assert is_balanced_parentheses("(hello[world]{test)") == False