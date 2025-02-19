import pytest
from src.max_balanced_parentheses import max_balanced_parentheses_pairs

def test_max_balanced_parentheses_pairs():
    # Test cases with different scenarios
    assert max_balanced_parentheses_pairs("(())()")  == 3
    assert max_balanced_parentheses_pairs("((()))")  == 3
    assert max_balanced_parentheses_pairs("()()()") == 3
    assert max_balanced_parentheses_pairs("(())()") == 3
    
    # Edge cases
    assert max_balanced_parentheses_pairs("") == 0
    assert max_balanced_parentheses_pairs("()") == 1
    
    # Unbalanced cases
    assert max_balanced_parentheses_pairs("(((") == 0
    assert max_balanced_parentheses_pairs(")))") == 0
    
    # Mixed characters
    assert max_balanced_parentheses_pairs("(a)b()c)") == 1
    assert max_balanced_parentheses_pairs("(()())((()))") == 6

def test_type_hint():
    # Type checking
    result = max_balanced_parentheses_pairs("(())")
    assert isinstance(result, int), "Function should return an integer"