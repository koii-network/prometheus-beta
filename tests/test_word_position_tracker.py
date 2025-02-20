import pytest
from src.word_position_tracker import track_word_positions

def test_basic_word_tracking():
    text = "the quick brown fox jumps over the lazy dog"
    result = track_word_positions(text)
    
    # Check basic tracking
    assert "the" in result
    assert result["the"] == [0, 5]
    assert len(result) == 8  # 8 unique words

def test_empty_string():
    text = ""
    result = track_word_positions(text)
    
    # Empty string should return empty dictionary
    assert result == {}

def test_single_word():
    text = "hello"
    result = track_word_positions(text)
    
    # Single word should have position [0]
    assert result == {"hello": [0]}

def test_repeated_words():
    text = "apple banana apple cherry banana apple"
    result = track_word_positions(text)
    
    # Check if positions are tracked correctly
    assert result["apple"] == [0, 2, 5]
    assert result["banana"] == [1, 4]
    assert result["cherry"] == [3]

def test_case_insensitivity():
    text = "Hello hello HELLO world World"
    result = track_word_positions(text)
    
    # All variations of 'hello' should be treated as the same word
    assert result["hello"] == [0, 1, 2]
    assert result["world"] == [3, 4]

def test_whitespace_handling():
    text = "  hello   world  test  "
    result = track_word_positions(text)
    
    # Whitespace should be handled correctly
    assert len(result) == 3
    assert "hello" in result
    assert "world" in result
    assert "test" in result
    assert result["hello"] == [0]
    assert result["world"] == [1]
    assert result["test"] == [2]