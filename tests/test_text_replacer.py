import pytest
from src.text_replacer import replace_words

def test_basic_replacement():
    """Test basic word replacement"""
    assert replace_words("hello world", {"hello": "hi", "world": "earth"}) == "hi earth"

def test_partial_replacement():
    """Test when only some words are replaced"""
    assert replace_words("the quick brown fox", {"quick": "lazy"}) == "the lazy brown fox"

def test_no_replacements():
    """Test when no replacements match"""
    assert replace_words("hello world", {"cat": "dog"}) == "hello world"

def test_empty_input():
    """Test with empty input string"""
    assert replace_words("", {"hello": "world"}) == ""

def test_empty_replacements():
    """Test with empty replacements dictionary"""
    assert replace_words("hello world", {}) == "hello world"

def test_case_sensitive():
    """Test that replacements are case-sensitive"""
    assert replace_words("Hello HELLO hello", {"hello": "hi"}) == "Hello HELLO hi"

def test_multiple_same_replacements():
    """Test replacing multiple occurrences of the same word"""
    assert replace_words("hello hello world", {"hello": "hi"}) == "hi hi world"