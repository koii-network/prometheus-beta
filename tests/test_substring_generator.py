import pytest
from src.substring_generator import generate_substrings

def test_generate_substrings_normal_case():
    """Test substring generation for a simple string."""
    result = generate_substrings("abc")
    expected = ["a", "ab", "abc", "b", "bc", "c"]
    assert sorted(result) == sorted(expected)

def test_generate_substrings_empty_string():
    """Test substring generation for an empty string."""
    result = generate_substrings("")
    assert result == []

def test_generate_substrings_single_char():
    """Test substring generation for a single character string."""
    result = generate_substrings("x")
    assert result == ["x"]

def test_generate_substrings_with_spaces_and_symbols():
    """Test substring generation with spaces and symbols."""
    result = generate_substrings("hello world!")
    assert len(result) == 66  # Total possible substrings
    assert "hello" in result
    assert " " in result
    assert "hello world!" in result

def test_generate_substrings_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_substrings(123)
        generate_substrings(None)