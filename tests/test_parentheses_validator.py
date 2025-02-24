import pytest
from src.parentheses_validator import is_balanced_parentheses

def test_balanced_parentheses():
    """Test various balanced parentheses scenarios."""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("()()") == True
    assert is_balanced_parentheses("(())()") == True
    assert is_balanced_parentheses("") == True

def test_unbalanced_parentheses():
    """Test various unbalanced parentheses scenarios."""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())") == False

def test_complex_balanced_parentheses():
    """Test more complex balanced parentheses patterns."""
    assert is_balanced_parentheses("((()()))") == True
    assert is_balanced_parentheses("(()())(())") == True

def test_invalid_input():
    """Test inputs with non-parentheses characters."""
    assert is_balanced_parentheses("(a)") == False
    assert is_balanced_parentheses("hello") == False
    assert is_balanced_parentheses("(1)") == False