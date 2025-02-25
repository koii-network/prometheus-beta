import pytest
from src.string_converter import to_alternate_path_case

def test_basic_conversion():
    assert to_alternate_path_case("hello world") == 'hello-WORLD'
    assert to_alternate_path_case("python programming") == 'python-PROGRAMMING'

def test_multiple_words():
    assert to_alternate_path_case("this is a test") == 'this-IS-a-TEST'

def test_single_word():
    assert to_alternate_path_case("hello") == 'hello'

def test_empty_string():
    assert to_alternate_path_case("") == ''

def test_mixed_case():
    assert to_alternate_path_case("PYTHON snake CASE") == 'python-SNAKE-case'

def test_invalid_input():
    with pytest.raises(TypeError):
        to_alternate_path_case(123)
    with pytest.raises(TypeError):
        to_alternate_path_case(None)