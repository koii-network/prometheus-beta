import pytest
from src.longest_word import find_longest_word

def test_normal_sentence():
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_multiple_longest_words():
    assert find_longest_word("hello world python") == "hello"

def test_single_word():
    assert find_longest_word("programming") == "programming"

def test_sentences_with_punctuation():
    assert find_longest_word("Hello, world! Python is great.") == "Python"

def test_case_sensitivity():
    assert find_longest_word("Short LONGER longest") == "longest"

def test_empty_string_raises_error():
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("")
    
def test_whitespace_only_raises_error():
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("   \t\n")

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(["hello", "world"])