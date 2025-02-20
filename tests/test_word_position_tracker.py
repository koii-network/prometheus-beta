import pytest
from src.word_position_tracker import track_word_positions

def test_basic_word_position_tracking():
    """Test tracking word positions in a simple sentence."""
    text = "hello world hello"
    result = track_word_positions(text)
    assert result == {'hello': [0, 2], 'world': [1]}

def test_case_insensitivity():
    """Test that word tracking is case-insensitive."""
    text = "Hello HELLO hello"
    result = track_word_positions(text)
    assert result == {'hello': [0, 1, 2]}

def test_empty_string():
    """Test tracking word positions in an empty string."""
    text = ""
    result = track_word_positions(text)
    assert result == {}

def test_sentence_with_punctuation():
    """Test tracking word positions in a sentence with punctuation."""
    text = "Hello, world! Hello, how are you?"
    result = track_word_positions(text)
    assert result == {
        'hello': [0, 2],
        'world': [1],
        'how': [3],
        'are': [4],
        'you': [5]
    }

def test_long_text():
    """Test tracking word positions in a longer text."""
    text = "the quick brown fox jumps over the lazy dog the fox"
    result = track_word_positions(text)
    assert result == {
        'the': [0, 6, 9],
        'quick': [1],
        'brown': [2],
        'fox': [3, 10],
        'jumps': [4],
        'over': [5],
        'lazy': [7],
        'dog': [8]
    }