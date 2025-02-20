import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    assert is_anagram('listen', 'silent') is True
    assert is_anagram('hello', 'olleh') is True
    assert is_anagram('debit card', 'bad credit') is True

def test_non_anagrams():
    assert is_anagram('python', 'ruby') is False
    assert is_anagram('cat', 'dog') is False
    assert is_anagram('hello', 'world') is False

def test_same_string():
    assert is_anagram('test', 'test') is True
    assert is_anagram('', '') is True

def test_different_lengths():
    assert is_anagram('short', 'longer') is False
    assert is_anagram('a', 'ab') is False

def test_invalid_input():
    with pytest.raises(ValueError, match="Input strings must contain only lowercase letters"):
        is_anagram('Hello', 'hello')
    
    with pytest.raises(ValueError, match="Input strings must contain only lowercase letters"):
        is_anagram('hello', 'Hello!')

def test_empty_strings():
    assert is_anagram('', '') is True

def test_repeated_characters():
    assert is_anagram('aab', 'baa') is True
    assert is_anagram('aab', 'aba') is True
    assert is_anagram('aaab', 'baaa') is True
    assert is_anagram('aab', 'bba') is False