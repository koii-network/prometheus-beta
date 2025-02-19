import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_balanced_parentheses():
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("(()())") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("") == True

def test_unbalanced_parentheses():
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())") == False
    assert is_balanced_parentheses("(())(()") == False

def test_invalid_characters():
    with pytest.raises(AssertionError):
        is_balanced_parentheses("(a)")
        is_balanced_parentheses("123")
        is_balanced_parentheses("[]{}")