import pytest
from src.parity_subsequence import find_longest_parity_subsequence

def test_mixed_parity_sequence():
    # Mixed parity sequence with multiple subsequences
    assert find_longest_parity_subsequence([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]
    assert find_longest_parity_subsequence([1, 3, 5, 7, 2, 4, 6]) == [1, 3, 5, 7]

def test_all_even_sequence():
    # All even sequence
    assert find_longest_parity_subsequence([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]

def test_all_odd_sequence():
    # All odd sequence
    assert find_longest_parity_subsequence([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_empty_sequence():
    # Empty input
    assert find_longest_parity_subsequence([]) == []

def test_single_element_sequences():
    # Single even element
    assert find_longest_parity_subsequence([2]) == [2]
    
    # Single odd element
    assert find_longest_parity_subsequence([1]) == [1]

def test_complex_mixed_sequence():
    # Complex mixed sequence
    assert find_longest_parity_subsequence([1, 2, 3, 4, 5, 6, 1, 3, 5]) == [1, 3, 5]
    assert find_longest_parity_subsequence([2, 4, 1, 3, 5, 6, 8, 10]) == [6, 8, 10]