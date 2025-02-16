import pytest
from src.json_validator import is_valid_json

def test_valid_json_objects():
    valid_jsons = [
        '{"name": "John", "age": 30}',
        '[]',
        '{"items": [1, 2, 3]}',
        '{"nested": {"a": 1, "b": 2}}',
        '12',
        '"string"',
        'null'
    ]
    
    for json_str in valid_jsons:
        assert is_valid_json(json_str) == True, f"Failed for {json_str}"

def test_invalid_json_objects():
    invalid_jsons = [
        '{name: "John"}',  # Missing quotes
        "{'key': 'value'}",  # Single quotes
        '{"incomplete"',  # Missing closing brace
        '{"extra": 1,}',  # Trailing comma
        ''
    ]
    
    for json_str in invalid_jsons:
        assert is_valid_json(json_str) == False, f"Failed for {json_str}"

def test_edge_cases():
    assert is_valid_json(None) == False
    assert is_valid_json(123) == False
    assert is_valid_json([]) == False