import pytest
from src.string_reversal import (
    reverse_string_manual, 
    reverse_string_reversed,
    reverse_string_slicing,
    reverse_string_split_reverse_join,
    reverse_string_recursive
)

# Test cases to ensure all methods work consistently
@pytest.mark.parametrize("reversal_func", [
    reverse_string_manual,
    reverse_string_reversed,
    reverse_string_slicing,
    reverse_string_split_reverse_join,
    reverse_string_recursive
])
def test_string_reversal_methods(reversal_func):
    # Test normal string
    assert reversal_func("hello") == "olleh"
    
    # Test empty string
    assert reversal_func("") == ""
    
    # Test single character
    assert reversal_func("a") == "a"
    
    # Test string with spaces
    assert reversal_func("hello world") == "dlrow olleh"
    
    # Test string with special characters
    assert reversal_func("a1b2c3") == "3c2b1a"

# Additional test to ensure all methods produce the same output
def test_all_methods_consistent():
    test_strings = [
        "hello", 
        "", 
        "a", 
        "hello world", 
        "a1b2c3"
    ]
    
    for test_str in test_strings:
        results = set([
            reverse_string_manual(test_str),
            reverse_string_reversed(test_str),
            reverse_string_slicing(test_str),
            reverse_string_split_reverse_join(test_str),
            reverse_string_recursive(test_str)
        ])
        assert len(results) == 1, f"Inconsistent results for {test_str}"