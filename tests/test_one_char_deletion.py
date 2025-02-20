import pytest
from src.one_char_deletion import can_convert_by_one_deletion

def test_can_convert_by_one_deletion():
    # Test cases where conversion is possible
    assert can_convert_by_one_deletion("abcd", "abc") == True  # delete 'd'
    assert can_convert_by_one_deletion("abcd", "abd") == True  # delete 'c'
    assert can_convert_by_one_deletion("abcd", "acd") == True  # delete 'b'
    assert can_convert_by_one_deletion("abcd", "bcd") == True  # delete 'a'
    
    # Test cases where conversion is not possible
    assert can_convert_by_one_deletion("abcd", "ab") == False  # too short
    assert can_convert_by_one_deletion("abcd", "abce") == False  # too long
    assert can_convert_by_one_deletion("abcd", "abcd") == False  # same string
    assert can_convert_by_one_deletion("abc", "abcd") == False  # can't add characters
    
    # Edge cases
    assert can_convert_by_one_deletion("a", "") == True
    assert can_convert_by_one_deletion("", "a") == False
    
    # Empty string cases
    assert can_convert_by_one_deletion("", "") == False