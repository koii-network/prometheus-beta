import pytest
from src.parentheses_validator import is_correctly_nested

def test_empty_string():
    assert is_correctly_nested('') == True

def test_simple_valid_cases():
    assert is_correctly_nested('()') == True
    assert is_correctly_nested('(())') == True
    assert is_correctly_nested('((()))') == True
    assert is_correctly_nested('(()())') == True

def test_invalid_cases():
    assert is_correctly_nested('(') == False
    assert is_correctly_nested(')') == False
    assert is_correctly_nested('())') == False
    assert is_correctly_nested('((()') == False
    assert is_correctly_nested(')(') == False

def test_mixed_strings():
    assert is_correctly_nested('a(b)c') == True
    assert is_correctly_nested('hello(world)') == True
    assert is_correctly_nested('(hello(world))') == True
    assert is_correctly_nested('hello(world') == False
    assert is_correctly_nested('(hello)world)') == False