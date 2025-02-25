import pytest
from src.parentheses_validator import is_valid_parentheses

def test_simple_valid_parentheses():
    """Test simple valid parentheses string"""
    assert is_valid_parentheses("()") == True

def test_nested_valid_parentheses():
    """Test nested valid parentheses"""
    assert is_valid_parentheses("(())") == True

def test_multiple_valid_parentheses():
    """Test multiple valid parentheses groups"""
    assert is_valid_parentheses("()()") == True

def test_complex_valid_parentheses():
    """Test complex valid parentheses arrangement"""
    assert is_valid_parentheses("((()))") == True

def test_invalid_unbalanced_opening():
    """Test unbalanced opening parentheses"""
    assert is_valid_parentheses("(()") == False

def test_invalid_unbalanced_closing():
    """Test unbalanced closing parentheses"""
    assert is_valid_parentheses("())") == False

def test_invalid_reversed_order():
    """Test reversed parentheses order"""
    assert is_valid_parentheses(")(") == False

def test_empty_string():
    """Test empty string is considered valid"""
    assert is_valid_parentheses("") == True

def test_only_left_parentheses():
    """Test string with only left parentheses"""
    assert is_valid_parentheses("(((") == False

def test_only_right_parentheses():
    """Test string with only right parentheses"""
    assert is_valid_parentheses(")))") == False