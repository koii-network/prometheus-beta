import pytest
from src.text_replacer import replace_words

def test_basic_replacement():
    """Test basic word replacement."""
    text = "hello world"
    replacements = {"hello": "hi"}
    assert replace_words(text, replacements) == "hi world"

def test_multiple_replacements():
    """Test multiple word replacements."""
    text = "the quick brown fox jumps over the lazy dog"
    replacements = {"quick": "slow", "brown": "red", "lazy": "alert"}
    result = replace_words(text, replacements)
    assert result == "the slow red fox jumps over the alert dog"

def test_overlapping_replacements():
    """Test replacements that could cause partial replacements."""
    text = "catcatastrophe"
    replacements = {"cat": "dog", "catastrophe": "disaster"}
    result = replace_words(text, replacements)
    assert result == "dogdogdisaster"

def test_empty_inputs():
    """Test with empty string and empty replacements."""
    assert replace_words("", {}) == ""

def test_no_replacements():
    """Test when no replacements match."""
    text = "hello world"
    replacements = {"test": "replacement"}
    assert replace_words(text, replacements) == text

def test_invalid_inputs():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input text must be a string"):
        replace_words(123, {})
    
    with pytest.raises(TypeError, match="Replacements must be a dictionary"):
        replace_words("text", "not a dict")