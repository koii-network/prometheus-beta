import pytest
from src.text_word_splitter import split_text_into_words

def test_basic_text_splitting():
    # Test basic splitting with capital letters and punctuation
    text = "HelloWorld.ThisIsATest"
    assert split_text_into_words(text) == ["Hello", "World.", "This", "Is", "A", "Test"]

def test_punctuation_handling():
    # Test handling of punctuation marks
    text = "Hello,World!How.Are.You?"
    assert split_text_into_words(text) == ["Hello,", "World!", "How.", "Are.", "You?"]

def test_capital_letter_sequences():
    # Test sequences of capital letters
    text = "ABCDefghIJKLmno"
    assert split_text_into_words(text) == ["A", "B", "C", "Def", "ghi", "J", "K", "L", "mno"]

def test_quoted_text():
    # Test text with quotation marks
    text = "He\"said\"HelloWorld"
    assert split_text_into_words(text) == ["He\"said\"", "Hello", "World"]

def test_mixed_case_and_punctuation():
    # Test a mix of capital letters, punctuation, and quotations
    text = "Hello,World!ThisIs\"ATest\".WithMixedElements"
    assert split_text_into_words(text) == ["Hello,", "World!", "This", "Is\"A", "Test\".", "With", "Mixed", "Elements"]

def test_empty_string():
    # Test empty string input
    text = ""
    assert split_text_into_words(text) == []

def test_single_word():
    # Test single word input
    text = "HelloWorld"
    assert split_text_into_words(text) == ["Hello", "World"]