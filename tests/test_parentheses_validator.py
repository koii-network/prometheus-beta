import pytest
from src.parentheses_validator import is_balanced_parentheses

def test_balanced_simple_parentheses():
    assert is_balanced_parentheses('()') == True

def test_balanced_nested_parentheses():
    assert is_balanced_parentheses('([{}])') == True

def test_balanced_mixed_parentheses():
    assert is_balanced_parentheses('({[]})') == True

def test_unbalanced_mismatched_parentheses():
    assert is_balanced_parentheses('([)]') == False

def test_unbalanced_extra_opening():
    assert is_balanced_parentheses('((()') == False

def test_unbalanced_extra_closing():
    assert is_balanced_parentheses('())') == False

def test_empty_string():
    assert is_balanced_parentheses('') == True

def test_string_with_no_parentheses():
    assert is_balanced_parentheses('hello world') == True

def test_complex_mixed_string():
    assert is_balanced_parentheses('a(b[c{d}e]f)g') == True

def test_complex_unbalanced_string():
    assert is_balanced_parentheses('a(b[c{d}e)f]g') == False