import pytest
from src.count_a_chars import count_a_chars

def test_count_a_chars():
    # Test basic cases
    assert count_a_chars("apple") == 1
    assert count_a_chars("banana") == 3
    assert count_a_chars("APPLE") == 1
    assert count_a_chars("ApPlE") == 1
    
    # Test case sensitivity
    assert count_a_chars("AaAaA") == 5
    
    # Test empty string
    assert count_a_chars("") == 0
    
    # Test string with no 'a'
    assert count_a_chars("hello") == 0
    
    # Test error handling for non-string input
    with pytest.raises(TypeError):
        count_a_chars(123)
    
    with pytest.raises(TypeError):
        count_a_chars(None)