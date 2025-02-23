import pytest
from src.substring_reversal import reverse_substring

def test_basic_substring_reversal():
    """Test basic substring reversal in the middle of a string."""
    assert reverse_substring("hello world", 1, 4) == "hlleo world"

def test_full_string_reversal():
    """Test reversing the entire string."""
    assert reverse_substring("python", 0, 6) == "nohtyp"

def test_empty_string_reversal():
    """Test reversing an empty string."""
    assert reverse_substring("", 0, 0) == ""

def test_single_character_string():
    """Test reversing a single character string."""
    assert reverse_substring("a", 0, 1) == "a"

def test_invalid_start_index():
    """Test raising ValueError for negative start index."""
    with pytest.raises(ValueError):
        reverse_substring("hello", -1, 3)

def test_invalid_end_index():
    """Test raising ValueError for end index beyond string length."""
    with pytest.raises(ValueError):
        reverse_substring("hello", 1, 10)

def test_start_index_greater_than_end_index():
    """Test raising ValueError when start index is greater than end index."""
    with pytest.raises(ValueError):
        reverse_substring("hello", 3, 2)

def test_type_errors():
    """Test raising TypeError for invalid input types."""
    with pytest.raises(TypeError):
        reverse_substring(123, 0, 3)
    
    with pytest.raises(TypeError):
        reverse_substring("hello", "0", 3)
    
    with pytest.raises(TypeError):
        reverse_substring("hello", 0, "3")

def test_substring_at_start():
    """Test reversing a substring at the start of the string."""
    assert reverse_substring("python", 0, 3) == "typhon"

def test_substring_at_end():
    """Test reversing a substring at the end of the string."""
    assert reverse_substring("python", 3, 6) == "pytnoh"