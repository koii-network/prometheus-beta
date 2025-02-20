import pytest
from src.string_reversal import (
    reverse_string, 
    manual_reverse, 
    reversed_method, 
    slicing_method, 
    split_reverse_method, 
    recursive_reverse
)

TEST_CASES = [
    "",             # Empty string
    "hello",        # Lowercase string
    "Hello World",  # Mixed case string with space
    "12345",        # Numeric string
    "Racecar",      # Mixed case palindrome
]

def test_all_reversal_methods():
    for test_str in TEST_CASES:
        # Test returning all methods
        result = reverse_string(test_str)
        assert isinstance(result, dict)
        assert len(result) == 5
        
        # Check that all results are correct
        expected = test_str[::-1]
        for method, reversed_str in result.items():
            assert reversed_str == expected, f"Failed for {method} method"

def test_specific_methods():
    methods = ['manual', 'reversed', 'slicing', 'split_reverse', 'recursive']
    test_str = "hello world"
    expected = test_str[::-1]
    
    for method in methods:
        result = reverse_string(test_str, method)
        assert result == expected, f"Failed for {method} method"

def test_invalid_method():
    with pytest.raises(ValueError):
        reverse_string("test", method="invalid_method")

def test_non_string_input():
    with pytest.raises(TypeError):
        reverse_string(12345)

def test_individual_methods():
    test_str = "hello"
    expected = test_str[::-1]
    
    assert manual_reverse(test_str) == expected
    assert reversed_method(test_str) == expected
    assert slicing_method(test_str) == expected
    assert split_reverse_method(test_str) == expected
    assert recursive_reverse(test_str) == expected