import pytest
from src.json_validator import is_valid_json

def test_valid_json_object():
    assert is_valid_json('{"name": "John", "age": 30}') == True

def test_valid_json_array():
    assert is_valid_json('[1, 2, 3, 4]') == True

def test_valid_json_nested():
    assert is_valid_json('{"users": [{"name": "Alice"}, {"name": "Bob"}]}') == True

def test_invalid_json_missing_quotes():
    assert is_valid_json('{name: "John"}') == False

def test_invalid_json_trailing_comma():
    assert is_valid_json('{"name": "John",}') == False

def test_invalid_json_syntax():
    assert is_valid_json('{"name": "John"') == False

def test_empty_string():
    assert is_valid_json('') == False

def test_non_string_input():
    assert is_valid_json(123) == False