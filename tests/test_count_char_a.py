import pytest
from src.count_char_a import count_char_a

def test_count_char_a():
    # Test cases with various scenarios
    assert count_char_a("Apple") == 1
    assert count_char_a("banana") == 3
    assert count_char_a("AMAZING") == 2
    assert count_char_a("hello world") == 0
    assert count_char_a("AaAaA") == 5
    
def test_count_char_a_empty_string():
    assert count_char_a("") == 0
    
def test_count_char_a_case_insensitive():
    assert count_char_a("AbracAdabra") == 5  # Mixed case
    assert count_char_a("AABBCCAA") == 4  # All uppercase
    assert count_char_a("aabbccaa") == 4  # All lowercase