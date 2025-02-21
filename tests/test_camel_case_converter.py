import pytest
from src.camel_case_converter import to_camel_case

def test_to_camel_case_basic_space_separated():
    assert to_camel_case('hello world') == 'helloWorld'
    assert to_camel_case('hello world python') == 'helloWorldPython'

def test_to_camel_case_hyphen_separated():
    assert to_camel_case('hello-world') == 'helloWorld'
    assert to_camel_case('snake-case-test') == 'snakeCaseTest'

def test_to_camel_case_underscore_separated():
    assert to_camel_case('hello_world') == 'helloWorld'
    assert to_camel_case('snake_case_test') == 'snakeCaseTest'

def test_to_camel_case_mixed_separators():
    assert to_camel_case('hello world-test_python') == 'helloWorldTestPython'

def test_to_camel_case_edge_cases():
    assert to_camel_case('') == ''
    assert to_camel_case('a') == 'a'
    assert to_camel_case('A') == 'a'

def test_to_camel_case_single_word_capitalization():
    assert to_camel_case('HELLO') == 'hello'
    assert to_camel_case('hello') == 'hello'