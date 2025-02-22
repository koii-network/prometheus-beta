import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_balanced_parentheses():
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("()()") == True
    assert is_balanced_parentheses("(()())") == True

def test_unbalanced_parentheses():
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("(()") == False
    assert is_balanced_parentheses("())") == False

def test_empty_string():
    assert is_balanced_parentheses("") == True

def test_complex_cases():
    assert is_balanced_parentheses("((()))()") == True
    assert is_balanced_parentheses("(()())(())") == True
    assert is_balanced_parentheses("((())(())())") == True
    assert is_balanced_parentheses("(((()") == False
    assert is_balanced_parentheses("())()") == False