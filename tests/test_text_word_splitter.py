import pytest
from src.text_word_splitter import split_text_to_words

def test_basic_splitting():
    assert split_text_to_words("HelloWorld") == ["Hello", "World"]
    assert split_text_to_words("helloWorld") == ["hello", "World"]

def test_punctuation_handling():
    assert split_text_to_words("Hello,World!") == ["Hello", ",", "World", "!"]
    assert split_text_to_words("hello.World?Test") == ["hello", ".", "World", "?", "Test"]

def test_multiple_capital_letters():
    assert split_text_to_words("HelloUnitedStates") == ["Hello", "United", "States"]
    assert split_text_to_words("helloUnitedStates") == ["hello", "United", "States"]

def test_quotation_marks():
    assert split_text_to_words("Hello\"World\"Test") == ["Hello", "World", "Test"]
    assert split_text_to_words("hello\"World\"test") == ["hello", "World", "test"]

def test_mixed_scenarios():
    assert split_text_to_words("Hello,UnitedStates!Test") == ["Hello", ",", "United", "States", "!", "Test"]
    assert split_text_to_words("hello.World?ImportantTest") == ["hello", ".", "World", "?", "Important", "Test"]

def test_edge_cases():
    assert split_text_to_words("") == []
    assert split_text_to_words("A") == ["A"]
    assert split_text_to_words("a") == ["a"]
    assert split_text_to_words("123Hello") == ["123", "Hello"]
    assert split_text_to_words("Hello123Test") == ["Hello", "123", "Test"]