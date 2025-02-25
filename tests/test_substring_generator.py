import pytest
from src.substring_generator import generate_all_substrings

def test_generate_all_substrings_normal_case():
    """Test substring generation for a typical string."""
    result = generate_all_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_generate_all_substrings_empty_string():
    """Test substring generation for an empty string."""
    result = generate_all_substrings("")
    assert result == []

def test_generate_all_substrings_single_char():
    """Test substring generation for a single character string."""
    result = generate_all_substrings("a")
    assert result == ['a']

def test_generate_all_substrings_special_chars():
    """Test substring generation with special characters."""
    result = generate_all_substrings("!@#")
    expected = ['!', '!@', '!@#', '@', '@#', '#']
    assert sorted(result) == sorted(expected)

def test_generate_all_substrings_repeated_chars():
    """Test substring generation with repeated characters."""
    result = generate_all_substrings("aaa")
    expected = ['a', 'a', 'a', 'aa', 'aa', 'aaa']
    assert sorted(result) == sorted(expected)
    assert len(result) == 6

def test_generate_all_substrings_unicode():
    """Test substring generation with unicode characters."""
    result = generate_all_substrings("こんにちは")
    expected = ['こ', 'こん', 'こんに', 'こんにち', 'こんにちは', 
                'ん', 'んに', 'んにち', 'んにちは', 
                'に', 'にち', 'にちは', 
                'ち', 'ちは', 
                'は']
    assert sorted(result) == sorted(expected)