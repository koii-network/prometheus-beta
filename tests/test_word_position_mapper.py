import pytest
from src.word_position_mapper import map_word_positions

def test_basic_word_position_mapping():
    """Test basic word position mapping"""
    text = "the quick brown fox jumps over the lazy dog"
    result = map_word_positions(text)
    
    assert result == {
        'the': [0, 5],
        'quick': [1],
        'brown': [2],
        'fox': [3],
        'jumps': [4],
        'over': [5],
        'lazy': [6],
        'dog': [7]
    }

def test_case_insensitivity():
    """Test that word mapping is case-insensitive"""
    text = "Hello hello HELLO world World"
    result = map_word_positions(text)
    
    assert result == {
        'hello': [0, 1, 2],
        'world': [3, 4]
    }

def test_empty_string():
    """Test mapping with an empty string"""
    text = ""
    result = map_word_positions(text)
    
    assert result == {}

def test_single_word():
    """Test mapping with a single word"""
    text = "python"
    result = map_word_positions(text)
    
    assert result == {'python': [0]}

def test_repeated_words_with_spaces():
    """Test mapping with repeated words and varying whitespace"""
    text = "apple   apple APPLE     apple"
    result = map_word_positions(text)
    
    assert result == {
        'apple': [0, 1, 2, 3]
    }

def test_punctuation_stripped():
    """Test that punctuation is not handled specially"""
    text = "hello, world! Hello, World."
    result = map_word_positions(text)
    
    assert result == {
        'hello,': [0, 3],
        'world!': [1],
        'hello,': [3],
        'world.': [4]
    }