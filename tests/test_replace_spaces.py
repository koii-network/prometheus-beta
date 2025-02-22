import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_replace_spaces_with_underscores():
    # Test normal string with multiple spaces
    assert replace_spaces_with_underscores("hello world") == "hello_world"
    
    # Test string with multiple consecutive spaces
    assert replace_spaces_with_underscores("hello   world") == "hello___world"
    
    # Test string with leading and trailing spaces
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"
    
    # Test empty string
    assert replace_spaces_with_underscores("") == ""
    
    # Test string with no spaces
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_error_handling():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)