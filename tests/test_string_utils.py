import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_with_underscores():
    # Test basic space replacement
    assert replace_spaces_with_underscores("hello world") == "hello_world"
    
    # Test multiple spaces
    assert replace_spaces_with_underscores("hello   world") == "hello___world"
    
    # Test string with no spaces
    assert replace_spaces_with_underscores("helloworld") == "helloworld"
    
    # Test empty string
    assert replace_spaces_with_underscores("") == ""
    
    # Test string with leading and trailing spaces
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_with_underscores_none_input():
    # Test None input raises ValueError
    with pytest.raises(ValueError, match="Input string cannot be None"):
        replace_spaces_with_underscores(None)