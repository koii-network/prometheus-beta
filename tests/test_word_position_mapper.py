import pytest
from src.word_position_mapper import map_word_positions

def test_map_word_positions_basic():
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

def test_map_word_positions_case_insensitive():
    """Test case-insensitive mapping"""
    text = "Hello hello HELLO world World"
    result = map_word_positions(text)
    
    assert result == {
        'hello': [0, 1, 2],
        'world': [3, 4]
    }

def test_map_word_positions_empty_string():
    """Test with an empty string"""
    text = ""
    result = map_word_positions(text)
    
    assert result == {}

def test_map_word_positions_punctuation():
    """Test with punctuation and mixed case"""
    text = "Python, python! PYTHON is awesome, is it?"
    result = map_word_positions(text)
    
    assert result == {
        'python': [0, 1, 2],
        'is': [3, 5],
        'awesome': [4],
        'it': [6]
    }

def test_map_word_positions_single_word():
    """Test with a single word"""
    text = "hello"
    result = map_word_positions(text)
    
    assert result == {'hello': [0]}