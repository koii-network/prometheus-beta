import pytest
from src.consecutive_substring_sum import max_consecutive_substring_sum

def test_basic_consecutive_string():
    assert max_consecutive_substring_sum('abcde') == sum(ord(c) for c in 'abcde')

def test_multiple_consecutive_sequences():
    assert max_consecutive_substring_sum('abcdexyzabc') == sum(ord(c) for c in 'abc')

def test_single_char_string():
    assert max_consecutive_substring_sum('z') == ord('z')

def test_empty_string():
    assert max_consecutive_substring_sum('') == 0

def test_no_consecutive_chars():
    assert max_consecutive_substring_sum('acegik') == max(ord(c) for c in 'acegik')

def test_repeated_consecutive_chars():
    assert max_consecutive_substring_sum('aabbccddee') == sum(ord('d') + ord('e') for _ in range(2))

def test_invalid_input():
    with pytest.raises(ValueError):
        max_consecutive_substring_sum(123)

def test_mixed_consecutive_sequence():
    assert max_consecutive_substring_sum('abcmnpqrs') == sum(ord(c) for c in 'abc')