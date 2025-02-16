import pytest
from src.z_algorithm import z_algorithm

def test_z_algorithm_basic_match():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    result = z_algorithm(text, pattern)
    assert result == [10]

def test_z_algorithm_multiple_matches():
    text = "AAAAAAAA"
    pattern = "AAA"
    result = z_algorithm(text, pattern)
    assert result == [0, 1, 2, 3, 4]

def test_z_algorithm_no_match():
    text = "ABCDEFG"
    pattern = "XYZ"
    result = z_algorithm(text, pattern)
    assert result == []

def test_z_algorithm_pattern_longer_than_text():
    text = "SHORT"
    pattern = "VERYLONGPATTERN"
    result = z_algorithm(text, pattern)
    assert result == []

def test_z_algorithm_empty_inputs():
    assert z_algorithm("", "") == []
    assert z_algorithm("TEXT", "") == []
    assert z_algorithm("", "PATTERN") == []

def test_z_algorithm_case_sensitive():
    text = "AbCaBcAbC"
    pattern = "abc"
    result = z_algorithm(text, pattern)
    assert result == []  # Case-sensitive match

def test_z_algorithm_complex_pattern():
    text = "ACACACACTGACACAC"
    pattern = "ACACAC"
    result = z_algorithm(text, pattern)
    assert result == [0, 2, 4, 10]