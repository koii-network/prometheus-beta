import pytest
from src.delete_one_char import can_convert_by_deleting_one_char

def test_can_convert_by_deleting_one_char():
    # Test cases where conversion is possible
    assert can_convert_by_deleting_one_char("abc", "ab") == True
    assert can_convert_by_deleting_one_char("abc", "ac") == True
    assert can_convert_by_deleting_one_char("abc", "bc") == True
    
    # Test cases where conversion is not possible
    assert can_convert_by_deleting_one_char("abc", "abc") == False  # no deletion
    assert can_convert_by_deleting_one_char("abc", "a") == False  # too short
    assert can_convert_by_deleting_one_char("abc", "abcd") == False  # too long
    assert can_convert_by_deleting_one_char("abc", "def") == False  # completely different
    
    # Edge cases
    assert can_convert_by_deleting_one_char("a", "") == True
    assert can_convert_by_deleting_one_char("", "") == False
    
    # Longer word tests
    assert can_convert_by_deleting_one_char("hello", "hell") == True
    assert can_convert_by_deleting_one_char("hello", "helo") == True
    assert can_convert_by_deleting_one_char("hello", "hello") == False