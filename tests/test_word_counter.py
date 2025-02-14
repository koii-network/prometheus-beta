import pytest
from src.word_counter import count_words

def test_count_words_basic():
    """Test basic word counting."""
    assert count_words("Hello world") == 2
    assert count_words("One") == 1
    assert count_words("") == 0

def test_count_words_multiple_spaces():
    """Test counting words with multiple spaces."""
    assert count_words("Hello   world   test") == 3
    assert count_words("  spaces  at  edges  ") == 4

def test_count_words_edge_cases():
    """Test edge cases like None, empty string, and various whitespaces."""
    assert count_words(None) == 0
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("\t\n multiple \t\nwhitespace\n") == 2

def test_count_words_punctuation():
    """Test word counting with punctuation."""
    assert count_words("Hello, world! How are you?") == 5
    assert count_words("Hyphenated-word counts") == 3