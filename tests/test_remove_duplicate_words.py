import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words():
    # Test basic duplicate removal
    assert remove_duplicate_words("hello hello world") == "hello world"
    
    # Test multiple duplicate words
    assert remove_duplicate_words("the quick brown fox jumps the quick fox") == "the quick brown fox jumps"
    
    # Test no duplicates
    assert remove_duplicate_words("hello world python") == "hello world python"
    
    # Test empty string
    assert remove_duplicate_words("") == ""
    
    # Test single word with duplicates
    assert remove_duplicate_words("python python python") == "python"

def test_remove_duplicate_words_error_handling():
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(None)

def test_remove_duplicate_words_whitespace():
    # Test multiple whitespaces
    assert remove_duplicate_words("hello   hello   world") == "hello world"
    
    # Test mixed whitespace
    assert remove_duplicate_words(" hello hello  world ") == "hello world"