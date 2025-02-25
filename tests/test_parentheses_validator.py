import pytest
from src.parentheses_validator import is_nested_parentheses

def test_simple_nested_parentheses():
    """Test basic correct nesting"""
    assert is_nested_parentheses("()") == True

def test_multiple_nested_parentheses():
    """Test multiple levels of nesting"""
    assert is_nested_parentheses("(())") == True

def test_deeply_nested_parentheses():
    """Test deeply nested parentheses"""
    assert is_nested_parentheses("((()))") == True

def test_invalid_unbalanced_parentheses():
    """Test unbalanced parentheses"""
    assert is_nested_parentheses("(()") == False
    assert is_nested_parentheses("())") == False

def test_incorrect_order_parentheses():
    """Test incorrect parentheses order"""
    assert is_nested_parentheses(")(") == False

def test_empty_string():
    """Test empty string case"""
    assert is_nested_parentheses("") == True

def test_string_with_only_open_parentheses():
    """Test string with only open parentheses"""
    assert is_nested_parentheses("(((") == False

def test_string_with_only_close_parentheses():
    """Test string with only close parentheses"""
    assert is_nested_parentheses(")))") == False

def test_mixed_string_with_other_characters():
    """Test nested parentheses in a mixed string"""
    assert is_nested_parentheses("a(b)c") == True
    assert is_nested_parentheses("a)(b") == False

def test_complex_nested_cases():
    """Test various complex nesting scenarios"""
    assert is_nested_parentheses("(a(b)c)") == True
    assert is_nested_parentheses("((a)b(c))") == True
    assert is_nested_parentheses("(a(b)c))") == False