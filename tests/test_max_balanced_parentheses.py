import pytest
from src.max_balanced_parentheses import max_balanced_parentheses_pairs

def test_max_balanced_parentheses_pairs():
    # Test cases with different scenarios
    assert max_balanced_parentheses_pairs("(()())") == 3
    assert max_balanced_parentheses_pairs("((())") == 2
    assert max_balanced_parentheses_pairs("()") == 1
    assert max_balanced_parentheses_pairs("") == 0
    assert max_balanced_parentheses_pairs("((()))") == 3
    
def test_max_balanced_parentheses_pairs_mixed_chars():
    # Test with mixed characters
    assert max_balanced_parentheses_pairs("a(b)c()d(e)f") == 2
    assert max_balanced_parentheses_pairs("hello(world)") == 1
    
def test_max_balanced_parentheses_pairs_many_pairs():
    # Test with many potential pairs
    assert max_balanced_parentheses_pairs("(((())))") == 4
    assert max_balanced_parentheses_pairs("()()()()") == 4

def test_max_balanced_parentheses_pairs_unbalanced():
    # Test unbalanced strings
    assert max_balanced_parentheses_pairs("(((") == 0
    assert max_balanced_parentheses_pairs(")))") == 0
    
def test_max_balanced_parentheses_pairs_input_types():
    # Test different input types
    with pytest.raises(TypeError):
        max_balanced_parentheses_pairs(12345)
    with pytest.raises(TypeError):
        max_balanced_parentheses_pairs(None)