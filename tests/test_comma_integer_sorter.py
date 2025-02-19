import pytest
from src.comma_integer_sorter import sort_comma_integers

def test_standard_comma_separated_integers():
    """Test sorting of standard comma-separated integers"""
    assert sort_comma_integers("3,1,4,1,5,9") == [1, 1, 3, 4, 5, 9]

def test_with_non_integer_characters():
    """Test handling of strings with non-integer characters"""
    assert sort_comma_integers("10,abc,20,def,30") == [10, 20, 30]

def test_empty_string():
    """Test handling of an empty string"""
    assert sort_comma_integers("") == []

def test_single_integer():
    """Test handling of a single integer"""
    assert sort_comma_integers("42") == [42]

def test_mixed_formats():
    """Test mixed formats including whitespaces and invalid characters"""
    assert sort_comma_integers(" 5 , 2abc , 10def , 7 ") == [2, 5, 7, 10]

def test_negative_integers():
    """Test handling of negative integers"""
    assert sort_comma_integers("-3,1,-5,4") == [-5, -3, 1, 4]