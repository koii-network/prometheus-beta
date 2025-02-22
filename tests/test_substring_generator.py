import pytest
from src.substring_generator import generate_substrings

def test_generate_substrings_normal_case():
    """Test substring generation for a standard string."""
    result = generate_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_generate_substrings_empty_string():
    """Test substring generation for an empty string."""
    result = generate_substrings("")
    assert result == []

def test_generate_substrings_single_char():
    """Test substring generation for a single character string."""
    result = generate_substrings("x")
    assert result == ['x']

def test_generate_substrings_long_string():
    """Test substring generation for a longer string."""
    result = generate_substrings("hello")
    expected = ['h', 'he', 'hel', 'hell', 'hello', 
                'e', 'el', 'ell', 'ello', 
                'l', 'll', 'llo', 
                'l', 'lo', 
                'o']
    assert sorted(result) == sorted(expected)

def test_generate_substrings_non_string_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_substrings(123)
        generate_substrings(None)
        generate_substrings([])