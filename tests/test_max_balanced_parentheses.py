import pytest
from src.max_balanced_parentheses import max_balanced_parentheses_pairs

def test_max_balanced_parentheses_pairs():
    # Test equal number of open and close parentheses
    assert max_balanced_parentheses_pairs("()()") == 2
    
    # Test more open parentheses
    assert max_balanced_parentheses_pairs("((()))") == 3
    
    # Test more close parentheses
    assert max_balanced_parentheses_pairs(")))((()") == 2
    
    # Test single type of parenthesis
    assert max_balanced_parentheses_pairs("(("))") == 1
    
    # Test empty string
    assert max_balanced_parentheses_pairs("") == 0
    
    # Test string with no parentheses
    assert max_balanced_parentheses_pairs("abc") == 0
    
    # Test mixed characters
    assert max_balanced_parentheses_pairs("a(b)c()d") == 2
    
    # Test complex mixed scenario
    assert max_balanced_parentheses_pairs("(())())(") == 3