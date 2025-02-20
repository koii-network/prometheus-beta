import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_find_near_palindrome_pairs():
    # Test case 1: Basic near palindrome pairs
    test_input1 = ["abc", "cba", "def", "fed"]
    expected1 = [["abc", "cba"], ["def", "fed"]]
    assert sorted(find_near_palindrome_pairs(test_input1)) == sorted(expected1)
    
    # Test case 2: No near palindrome pairs
    test_input2 = ["hello", "world", "python"]
    assert find_near_palindrome_pairs(test_input2) == []
    
    # Test case 3: Empty input
    test_input3 = []
    assert find_near_palindrome_pairs(test_input3) == []
    
    # Test case 4: Mixed cases with near palindrome and non-near palindrome
    test_input4 = ["racecar", "radar", "hello", "olleh"]
    expected4 = [["hello", "olleh"]]
    assert sorted(find_near_palindrome_pairs(test_input4)) == sorted(expected4)
    
    # Test case 5: Longer strings
    test_input5 = ["abcde", "edcba", "fghij", "jihgf"]
    expected5 = [["abcde", "edcba"], ["fghij", "jihgf"]]
    assert sorted(find_near_palindrome_pairs(test_input5)) == sorted(expected5)

def test_edge_cases():
    # Test single character strings
    test_input_single = ["a", "b", "c"]
    assert find_near_palindrome_pairs(test_input_single) == []
    
    # Test duplicate strings
    test_input_duplicate = ["abc", "abc"]
    assert find_near_palindrome_pairs(test_input_duplicate) == []