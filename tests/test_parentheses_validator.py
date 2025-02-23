import pytest
from src.parentheses_validator import is_valid_parentheses

def test_basic_valid_parentheses():
    """Test basic valid parentheses arrangements"""
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("(())") == True
    assert is_valid_parentheses("()()") == True
    assert is_valid_parentheses("(()())") == True

def test_nested_parentheses():
    """Test more complex valid nested parentheses"""
    assert is_valid_parentheses("((()))") == True
    assert is_valid_parentheses("(()()())") == True

def test_invalid_parentheses():
    """Test invalid parentheses arrangements"""
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses(")") == False
    assert is_valid_parentheses(")(") == False
    assert is_valid_parentheses("((()") == False
    assert is_valid_parentheses("())") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_valid_parentheses("") == True  # Empty string
    assert is_valid_parentheses("   ") == True  # String with only spaces

def test_mixed_characters():
    """Test strings with mixed characters"""
    assert is_valid_parentheses("a(b)c") == True
    assert is_valid_parentheses("(a(b)c)") == True
    assert is_valid_parentheses("a(b(c)d)e") == True

def test_complex_invalid_cases():
    """Test more complex invalid cases"""
    assert is_valid_parentheses("((()") == False
    assert is_valid_parentheses("())()") == False
    assert is_valid_parentheses("((()())") == False