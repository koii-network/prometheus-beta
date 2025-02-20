import pytest
from src.text_replacer import replace_words

def test_basic_word_replacement():
    """Test basic single word replacement"""
    text = "hello world"
    replacements = {"hello": "hi"}
    assert replace_words(text, replacements) == "hi world"

def test_multiple_word_replacements():
    """Test multiple word replacements"""
    text = "the quick brown fox jumps over the lazy dog"
    replacements = {"quick": "slow", "brown": "grey", "lazy": "active"}
    assert replace_words(text, replacements) == "the slow grey fox jumps over the active dog"

def test_repeated_word_replacements():
    """Test replacement of repeated words"""
    text = "apple apple banana apple"
    replacements = {"apple": "orange"}
    assert replace_words(text, replacements) == "orange orange banana orange"

def test_no_replacements():
    """Test when no replacements are needed"""
    text = "hello world"
    replacements = {"cat": "dog"}
    assert replace_words(text, replacements) == text

def test_empty_input():
    """Test with empty string"""
    text = ""
    replacements = {"hello": "hi"}
    assert replace_words(text, replacements) == ""

def test_invalid_text_type():
    """Test raising TypeError for non-string text"""
    with pytest.raises(TypeError, match="Input text must be a string"):
        replace_words(123, {"hello": "hi"})

def test_invalid_replacements_type():
    """Test raising TypeError for non-dictionary replacements"""
    with pytest.raises(TypeError, match="Replacements must be a dictionary"):
        replace_words("hello", "not a dict")

def test_invalid_replacement_keys():
    """Test raising TypeError for non-string replacement keys or values"""
    with pytest.raises(TypeError, match="All replacement dictionary keys and values must be strings"):
        replace_words("hello", {123: "world"})
    
    with pytest.raises(TypeError, match="All replacement dictionary keys and values must be strings"):
        replace_words("hello", {"hello": 123})