import pytest
from src.longest_word import find_longest_word

def test_basic_sentence():
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_multiple_longest_words():
    assert find_longest_word("hello world python") == "python"

def test_single_word():
    assert find_longest_word("hello") == "hello"

def test_sentence_with_punctuation():
    assert find_longest_word("Hello, world! Programming is fun.") == "Programming"

def test_empty_sentence_raises_error():
    with pytest.raises(ValueError, match="Sentence cannot be empty"):
        find_longest_word("")
    
    with pytest.raises(ValueError, match="Sentence cannot be empty"):
        find_longest_word("   ")

def test_non_string_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(["hello", "world"])

def test_words_with_same_length():
    assert find_longest_word("cat dog rat") == "cat"