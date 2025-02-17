import pytest
from src.most_frequent_char import find_most_frequent_character

def test_find_most_frequent_character():
    # Test basic functionality
    assert find_most_frequent_character("aabbbcccc") == "c"
    assert find_most_frequent_character("hello") == "l"
    
    # Test case with multiple characters having same frequency
    assert find_most_frequent_character("aabbcc") == "a"
    
    # Test empty string
    assert find_most_frequent_character("") is None
    
    # Test single character string
    assert find_most_frequent_character("a") == "a"
    
    # Test string with spaces and special characters
    assert find_most_frequent_character("hello world!!!") == " "
    
    # Test error case with non-string input
    with pytest.raises(TypeError):
        find_most_frequent_character(123)
    
    with pytest.raises(TypeError):
        find_most_frequent_character(None)