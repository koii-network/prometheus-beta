import pytest
from src.max_consecutive_characters_sum import max_consecutive_characters_sum

def test_basic_consecutive_sequence():
    assert max_consecutive_characters_sum('abcd') == 394  # 97+98+99+100

def test_mixed_sequence():
    assert max_consecutive_characters_sum('abcxyz') == 394  # 'abcd' sequence

def test_repeated_characters():
    assert max_consecutive_characters_sum('aabb') == 194  # 97+97

def test_single_character():
    assert max_consecutive_characters_sum('a') == 97  # ASCII value of 'a'

def test_non_consecutive_sequence():
    assert max_consecutive_characters_sum('aceg') == 97  # only first character

def test_empty_string_raises_error():
    with pytest.raises(ValueError):
        max_consecutive_characters_sum('')

def test_non_string_input_raises_error():
    with pytest.raises(TypeError):
        max_consecutive_characters_sum(123)

def test_complex_sequence():
    assert max_consecutive_characters_sum('abcdefxyzpqr') == 394  # 'abcd' sequence