import pytest
from src.integer_parser import parse_and_sort_integers

def test_basic_integer_parsing():
    assert parse_and_sort_integers("1,2,3") == [1, 2, 3]

def test_unsorted_input():
    assert parse_and_sort_integers("3,1,2") == [1, 2, 3]

def test_non_integer_characters():
    assert parse_and_sort_integers("1a,2b,3c") == [1, 2, 3]

def test_mixed_valid_invalid_input():
    assert parse_and_sort_integers("1,abc,2,def,3") == [1, 2, 3]

def test_empty_string():
    assert parse_and_sort_integers("") == []

def test_whitespace_input():
    assert parse_and_sort_integers("  1  ,  2  ,  3  ") == [1, 2, 3]

def test_negative_numbers():
    assert parse_and_sort_integers("-3,-1,0,2") == [-3, -1, 0, 2]

def test_large_numbers():
    assert parse_and_sort_integers("1000000,500,1") == [1, 500, 1000000]