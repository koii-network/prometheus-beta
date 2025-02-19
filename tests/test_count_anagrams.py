import pytest
from src.count_anagrams import count_anagrams

def test_count_anagrams_basic():
    assert count_anagrams('abc') == 6  # permutations: a, b, c, ab, ac, bc, abc, acb, bac, bca, cab, cba

def test_count_anagrams_single_char():
    assert count_anagrams('a') == 1

def test_count_anagrams_repeated_chars():
    assert count_anagrams('aab') == 3  # a, b, aa, ab, aab, aab(different order)

def test_count_anagrams_invalid_input():
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('ABC')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('a1b')