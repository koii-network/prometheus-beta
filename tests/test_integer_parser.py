import pytest
from src.integer_parser import parse_and_sort_integers

def test_basic_parse_and_sort():
    assert parse_and_sort_integers("1,2,3") == [1, 2, 3]
    assert parse_and_sort_integers("3,1,2") == [1, 2, 3]

def test_with_non_integer_characters():
    assert parse_and_sort_integers("a1b,c2d,3e") == [1, 2, 3]
    assert parse_and_sort_integers("10,5,abc,15") == [5, 10, 15]

def test_mixed_input():
    assert parse_and_sort_integers("abc,def,123,456ghi") == [123, 456]

def test_empty_input():
    assert parse_and_sort_integers("") == []
    assert parse_and_sort_integers(",,,") == []

def test_large_numbers():
    assert parse_and_sort_integers("1000,500,100") == [100, 500, 1000]

def test_invalid_input():
    assert parse_and_sort_integers("abc,def,ghi") == []