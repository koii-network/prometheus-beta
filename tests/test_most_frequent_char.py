import pytest
from src.most_frequent_char import find_most_frequent_char

def test_find_most_frequent_char():
    # Test basic cases with clear most frequent character
    assert find_most_frequent_char("hello") == "l"
    assert find_most_frequent_char("aabbcccd") == "c"
    assert find_most_frequent_char("aaabbc") == "a"

def test_find_most_frequent_char_first_occurrence():
    # If multiple characters have the same max frequency, 
    # return the first one encountered
    assert find_most_frequent_char("aabbcc") == "a"

def test_find_most_frequent_char_with_spaces():
    # Test with spaces and mixed characters
    assert find_most_frequent_char("hello world") == " "
    assert find_most_frequent_char("a b c a b") == "a"

def test_find_most_frequent_char_single_char():
    # Test with single character string
    assert find_most_frequent_char("x") == "x"

def test_find_most_frequent_char_error_cases():
    # Test error handling
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    
    with pytest.raises(TypeError):
        find_most_frequent_char(None)
    
    with pytest.raises(ValueError):
        find_most_frequent_char("")