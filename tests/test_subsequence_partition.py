import pytest
from src.subsequence_partition import can_partition_subsequences

def test_valid_partitions():
    # Test cases that should return True
    assert can_partition_subsequences("aeiou") == True  # all vowels
    assert can_partition_subsequences("bcd") == True  # all consonants
    assert can_partition_subsequences("aabb") == True  # mixed valid partition
    assert can_partition_subsequences("aeioubc") == True  # mixed longer partition
    assert can_partition_subsequences("eebb") == True  # multiple valid subsequences

def test_invalid_partitions():
    # Test cases that should return False
    assert can_partition_subsequences("") == False  # empty string
    assert can_partition_subsequences("a") == False  # single character
    assert can_partition_subsequences("ab") == False  # mixed letters
    assert can_partition_subsequences("abc") == False  # cannot partition

def test_edge_cases():
    # Additional edge cases
    assert can_partition_subsequences("uuuu") == True  # repeated vowels
    assert can_partition_subsequences("bbbb") == True  # repeated consonants
    assert can_partition_subsequences("aabbccdd") == True  # alternating valid subsequences

def test_long_sequences():
    # Longer and more complex sequences
    assert can_partition_subsequences("aaeeiioouubbccddffgg") == True
    assert can_partition_subsequences("abcdefghijklmnop") == False