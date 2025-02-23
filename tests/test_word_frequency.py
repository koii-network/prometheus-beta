import pytest
from src.word_frequency import most_frequent_word

def test_basic_frequency():
    """Test finding the most frequent word in a simple sentence."""
    text = "the cat is in the hat"
    assert most_frequent_word(text) == "the"

def test_single_word():
    """Test when there's only one word in the input."""
    text = "hello"
    assert most_frequent_word(text) == "hello"

def test_multiple_words_same_frequency():
    """Test when multiple words have the same frequency."""
    text = "a b c a b c"
    result = most_frequent_word(text)
    assert result in ["a", "b", "c"]

def test_case_sensitive_lowercase():
    """Ensure function works with only lowercase letters."""
    text = "apple banana apple orange banana"
    assert most_frequent_word(text) == "apple"

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        most_frequent_word("")

def test_whitespace_only_input_raises_error():
    """Test that whitespace-only input raises a ValueError."""
    with pytest.raises(ValueError, match="Input text contains no words"):
        most_frequent_word("   ")

def test_invalid_characters_raises_error():
    """Test that input with uppercase or non-letter characters raises an error."""
    with pytest.raises(ValueError, match="Input must contain only lowercase letters and spaces"):
        most_frequent_word("Hello World")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase letters and spaces"):
        most_frequent_word("hello world! 123")

def test_long_text_frequency():
    """Test frequency in a longer text."""
    text = "the quick brown fox jumps over the lazy dog the fox is quick"
    assert most_frequent_word(text) == "the"