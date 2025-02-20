import pytest
from src.one_character_deletion import can_convert_by_one_deletion

def test_can_convert_by_one_deletion():
    # Valid conversions
    assert can_convert_by_one_deletion("abcd", "abc") == True
    assert can_convert_by_one_deletion("abcd", "abd") == True
    assert can_convert_by_one_deletion("abcd", "acd") == True
    
    # Invalid conversions
    assert can_convert_by_one_deletion("abcd", "abce") == False
    assert can_convert_by_one_deletion("abc", "abcd") == False
    assert can_convert_by_one_deletion("abc", "def") == False
    
    # Edge cases
    assert can_convert_by_one_deletion("a", "") == True
    assert can_convert_by_one_deletion("", "a") == False
    
    # Same length words
    assert can_convert_by_one_deletion("abc", "abc") == False
    
    # Multiple possible deletions
    assert can_convert_by_one_deletion("abcde", "abce") == False  # should require exactly one deletion