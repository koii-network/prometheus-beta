import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    assert find_longest_word("The quick brown fox") == "quick"

def test_find_longest_word_multiple_max_length():
    assert find_longest_word("Hello world python programming") == "programming"

def test_find_longest_word_single_word():
    assert find_longest_word("python") == "python"

def test_find_longest_word_with_punctuation():
    assert find_longest_word("Hello, world! Programming is fun.") == "Programming"

def test_find_longest_word_multiple_spaces():
    assert find_longest_word("  many    spaces   here  ") == "spaces"

def test_find_longest_word_invalid_input():
    with pytest.raises(ValueError, match="Input must be a string"):
        find_longest_word(123)

def test_find_longest_word_empty_string():
    with pytest.raises(ValueError, match="Input sentence is empty"):
        find_longest_word("")

def test_find_longest_word_only_whitespace():
    with pytest.raises(ValueError, match="Input sentence is empty"):
        find_longest_word("   \t\n  ")