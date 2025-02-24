import pytest
from src.substring_generator import generate_substrings

def test_generate_substrings_normal_string():
    """Test substring generation for a typical string."""
    result = generate_substrings("abc")
    assert set(result) == set(['a', 'ab', 'abc', 'b', 'bc', 'c'])
    assert len(result) == 6

def test_generate_substrings_empty_string():
    """Test substring generation for an empty string."""
    result = generate_substrings("")
    assert result == []

def test_generate_substrings_single_char():
    """Test substring generation for a single character string."""
    result = generate_substrings("x")
    assert result == ['x']

def test_generate_substrings_repeated_chars():
    """Test substring generation for a string with repeated characters."""
    result = generate_substrings("aaa")
    assert set(result) == set(['a', 'aa', 'aaa'])
    assert len(result) == 6

def test_generate_substrings_unicode():
    """Test substring generation with unicode characters."""
    result = generate_substrings("こんにちは")
    assert len(result) == 15  # Verify multiple substrings are generated
    assert "こん" in result
    assert "にちは" in result

def test_generate_substrings_special_chars():
    """Test substring generation with special characters."""
    result = generate_substrings("a!b@c#")
    assert set(result) == set(['a', 'a!', 'a!b', 'a!b@', 'a!b@c', 'a!b@c#', 
                                '!', '!b', '!b@', '!b@c', '!b@c#', 
                                'b', 'b@', 'b@c', 'b@c#', 
                                '@', '@c', '@c#', 
                                'c', 'c#', 
                                '#'])
    assert len(result) == 21