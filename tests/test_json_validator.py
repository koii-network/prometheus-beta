import pytest
from src.json_validator import is_valid_json

def test_valid_json_object():
    assert is_valid_json('{"key": "value"}') == True

def test_valid_json_array():
    assert is_valid_json('[1, 2, 3]') == True

def test_valid_json_nested():
    assert is_valid_json('{"nested": {"key": "value"}}') == True

def test_invalid_json_missing_quotes():
    assert is_valid_json('{key: "value"}') == False

def test_invalid_json_syntax():
    assert is_valid_json('{') == False

def test_invalid_json_trailing_comma():
    assert is_valid_json('{"key": "value",}') == False

def test_empty_string():
    assert is_valid_json('') == False

def test_none_input():
    assert is_valid_json(None) == False