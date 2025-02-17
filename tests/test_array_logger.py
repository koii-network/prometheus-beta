import pytest
from src.array_logger import log_array_as_table

def test_log_array_basic_string():
    result = log_array_as_table(["apple", "banana", "cherry"])
    assert result == "apple\nbanana\ncherry"

def test_log_array_numeric():
    result = log_array_as_table([1, 2, 3])
    assert result == "1\n2\n3"

def test_log_array_mixed_types():
    result = log_array_as_table([1, "two", 3.14])
    assert result == "1\ntwo\n3.14"

def test_log_array_with_headers():
    result = log_array_as_table(["apple", "banana", "cherry"], 
                                 headers=["Fruit1", "Fruit2", "Fruit3"])
    expected = "Fruit1 | Fruit2 | Fruit3\n----------------\napple | banana | cherry"
    assert result.replace(" ", "") == expected.replace(" ", "")

def test_log_array_empty():
    result = log_array_as_table([])
    assert result == ""

def test_log_array_invalid_type():
    with pytest.raises(TypeError):
        log_array_as_table("not a list")

def test_log_array_headers_mismatch():
    with pytest.raises(ValueError):
        log_array_as_table([1, 2, 3], headers=["a", "b"])