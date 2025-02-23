import pytest
from src.word_character_reverser import reverse_words_and_characters

def test_reverse_words_and_characters():
    # Test basic functionality
    assert reverse_words_and_characters("hello world") == "dlrow olleh"
    
    # Test multiple words
    assert reverse_words_and_characters("python is awesome") == "emosewa si nohtyp"
    
    # Test empty string
    assert reverse_words_and_characters("") == ""
    
    # Test single word
    assert reverse_words_and_characters("hello") == "olleh"
    
    # Test string with multiple spaces
    assert reverse_words_and_characters("  multiple   spaces  ") == "secaps elpitlum"
    
    # Test string with punctuation
    assert reverse_words_and_characters("hello, world!") == "!dlrow ,olleh"