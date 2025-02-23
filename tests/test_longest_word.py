import pytest
from src.longest_word import find_longest_word

def test_basic_sentence():
    """Test finding longest word in a simple sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_multiple_longest_words():
    """Test when multiple words have the same maximum length."""
    assert find_longest_word("apple banana grape") == "apple"

def test_sentence_with_punctuation():
    """Test sentence with punctuation."""
    assert find_longest_word("Hello, world! How are you?") == "Hello"

def test_single_word():
    """Test with a single word."""
    assert find_longest_word("programming") == "programming"

def test_words_with_numbers():
    """Test sentence with words containing numbers."""
    assert find_longest_word("code2 python3 javascript") == "javascript"

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Sentence cannot be empty"):
        find_longest_word("")

def test_whitespace_only_raises_error():
    """Test that whitespace-only input raises a ValueError."""
    with pytest.raises(ValueError, match="Sentence cannot be empty"):
        find_longest_word("   \t\n")

def test_non_string_input_raises_error():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)

def test_mixed_case_words():
    """Test finding longest word with mixed case."""
    assert find_longest_word("Cat ELEPHANT mouse") == "ELEPHANT"