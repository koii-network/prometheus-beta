import pytest
from src.substring_generator import generate_substrings

def test_generate_substrings_basic():
    # Test with a simple string
    result = generate_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_generate_substrings_empty():
    # Test with an empty string
    result = generate_substrings("")
    assert result == []

def test_generate_substrings_single_char():
    # Test with a single character
    result = generate_substrings("x")
    assert result == ['x']

def test_generate_substrings_repeated_chars():
    # Test with repeated characters
    result = generate_substrings("aaa")
    expected = ['a', 'a', 'a', 'aa', 'aa', 'aaa']
    assert sorted(result) == sorted(expected)

def test_generate_substrings_with_special_chars():
    # Test with special characters
    result = generate_substrings("a!b@c")
    expected = ['a', 'a!', 'a!b', 'a!b@', 'a!b@c', 
                '!', '!b', '!b@', '!b@c', 
                'b', 'b@', 'b@c', 
                '@', '@c', 
                'c']
    assert sorted(result) == sorted(expected)

def test_generate_substrings_invalid_input():
    # Test with invalid input type
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_substrings(123)
        generate_substrings(None)