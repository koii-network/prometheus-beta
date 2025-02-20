import pytest
from src.unique_character_counter import count_unique_characters

def test_count_unique_characters():
    # Test normal cases
    assert count_unique_characters("hello") == 4  # h, e, l, o
    assert count_unique_characters("aAaA") == 2   # a, A are different
    
    # Test edge cases
    assert count_unique_characters("") == 0       # Empty string
    assert count_unique_characters(" ") == 1      # Whitespace
    assert count_unique_characters("   ") == 1    # Multiple whitespaces
    assert count_unique_characters(None) == 0     # None input
    
    # Test more complex cases
    assert count_unique_characters("abcABC123") == 9  # Mixed case and numbers
    assert count_unique_characters("!!@@##") == 6     # Special characters