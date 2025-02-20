import pytest
from src.balanced_parentheses import is_balanced_parentheses

def test_balanced_parentheses():
    # Simple balanced cases
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("[]") == True
    assert is_balanced_parentheses("{}") == True
    
    # Nested balanced cases
    assert is_balanced_parentheses("([{}])") == True
    assert is_balanced_parentheses("{[()]}") == True
    assert is_balanced_parentheses("({[]})") == True
    
    # Unbalanced cases
    assert is_balanced_parentheses("(]") == False
    assert is_balanced_parentheses("([)]") == False
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses("]{") == False
    
    # Mixed content cases
    assert is_balanced_parentheses("hello(world)[test]{123}") == True
    assert is_balanced_parentheses("(a + b) * {c - [d]}") == True
    
    # Empty string case
    assert is_balanced_parentheses("") == True
    
    # Complex nested cases
    assert is_balanced_parentheses("((())){[()]()}") == True
    assert is_balanced_parentheses("((())){[()]()") == False