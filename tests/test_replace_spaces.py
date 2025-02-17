import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_replace_spaces_normal_string():
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_multiple_spaces():
    assert replace_spaces_with_underscores("hello  world  test") == "hello__world__test"

def test_replace_spaces_leading_trailing_spaces():
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_empty_string():
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_no_spaces():
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_invalid_input():
    with pytest.raises(TypeError):
        replace_spaces_with_underscores(123)
    with pytest.raises(TypeError):
        replace_spaces_with_underscores(None)