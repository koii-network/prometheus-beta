import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_basic_conversion():
    assert to_alternating_kebab_case("hello world") == 'helloWorld'
    assert to_alternating_kebab_case("PYTHON PROGRAMMING") == 'pythonProgramming'
    assert to_alternating_kebab_case("snake_case example") == 'snakeCaseExample'

def test_single_word():
    assert to_alternating_kebab_case("hello") == 'hello'
    assert to_alternating_kebab_case("WORLD") == 'world'

def test_multiple_words():
    assert to_alternating_kebab_case("one two three four") == 'oneTwothreeFour'

def test_empty_string():
    assert to_alternating_kebab_case("") == ''

def test_mixed_case_input():
    assert to_alternating_kebab_case("Hello WORLD python PROGRAMMING") == 'helloWorldpythonProgramming'

def test_input_with_existing_dashes():
    assert to_alternating_kebab_case("hello-world python-programming") == 'helloWorldpythonProgramming'

def test_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_kebab_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_kebab_case(None)

def test_special_characters():
    assert to_alternating_kebab_case("hello! world@") == 'helloWorld'
    assert to_alternating_kebab_case("python#code") == 'pythonCode'