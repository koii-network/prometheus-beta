import pytest
from src.longest_unique_substring import longest_unique_substring_length

def test_normal_cases():
    """Test typical input scenarios"""
    assert longest_unique_substring_length("abcabcbb") == 3
    assert longest_unique_substring_length("bbbbb") == 1
    assert longest_unique_substring_length("pwwkew") == 3

def test_edge_cases():
    """Test edge case scenarios"""
    assert longest_unique_substring_length("") == 0
    assert longest_unique_substring_length("a") == 1
    assert longest_unique_substring_length(" ") == 1
    assert longest_unique_substring_length("aab") == 2

def test_complex_cases():
    """Test more complex input scenarios"""
    assert longest_unique_substring_length("dvdf") == 3
    assert longest_unique_substring_length("tmmzuxt") == 5
    assert longest_unique_substring_length("abcdefghijklmnopqrstuvwxyz") == 26

def test_repeated_characters():
    """Test scenarios with repeated characters"""
    assert longest_unique_substring_length("abba") == 2
    assert longest_unique_substring_length("aaa") == 1

def test_unicode_characters():
    """Test support for Unicode characters"""
    assert longest_unique_substring_length("こんにちは") == 5
    assert longest_unique_substring_length("🌈🦄🌈") == 2