import pytest
from src.parentheses_validator import is_balanced_parentheses

def test_empty_string():
    assert is_balanced_parentheses("") == True

def test_simple_balanced_parentheses():
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("()()") == True

def test_nested_balanced_parentheses():
    assert is_balanced_parentheses("(()())") == True
    assert is_balanced_parentheses("((()))") == True

def test_unbalanced_parentheses():
    assert is_balanced_parentheses("(()") == False
    assert is_balanced_parentheses("())") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("((()") == False

def test_multiple_unbalanced_scenarios():
    assert is_balanced_parentheses("(()()") == False
    assert is_balanced_parentheses("())(()") == False

def test_complex_unbalanced_strings():
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("(()())())(") == False

@pytest.mark.parametrize("invalid_input", [
    "hello(world)",
    "12(34)",
    "a(b)c",
    "(test)",
    "(test)test"
])
def test_strings_with_additional_characters(invalid_input):
    # The function should still work correctly even with additional characters
    is_balanced_parentheses(invalid_input)