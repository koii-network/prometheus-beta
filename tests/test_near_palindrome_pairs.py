import sys
import os
import pytest

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_find_near_palindrome_pairs_basic():
    # Basic case with near palindrome pairs
    input_strings = ['racab', 'abcar', 'hello', 'olleh']
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) == 2
    assert ['racab', 'abcar'] in result or ['abcar', 'racab'] in result

def test_find_near_palindrome_pairs_empty():
    # Empty input list
    assert find_near_palindrome_pairs([]) == []

def test_find_near_palindrome_pairs_no_pairs():
    # No near palindrome pairs
    input_strings = ['hello', 'world', 'python']
    assert find_near_palindrome_pairs(input_strings) == []

def test_find_near_palindrome_pairs_single_character():
    # Test with single character strings
    input_strings = ['a', 'b', 'c', 'd']
    assert find_near_palindrome_pairs(input_strings) == []

def test_find_near_palindrome_pairs_mixed_case():
    # Test case sensitivity
    input_strings = ['Racab', 'abcar', 'Hello', 'olleh']
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) == 0  # Case-sensitive, so no pairs

def test_find_near_palindrome_pairs_edge_cases():
    # Complex edge cases
    input_strings = ['aaaab', 'baaaa', 'abcde', 'edcba']
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) == 2