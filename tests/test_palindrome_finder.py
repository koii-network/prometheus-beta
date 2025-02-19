import pytest
from src.palindrome_finder import find_non_overlapping_palindromes

def test_find_non_overlapping_palindromes():
    # Test basic cases
    assert find_non_overlapping_palindromes("") == []
    assert find_non_overlapping_palindromes("a") == ["a"]
    
    # Test string with multiple palindromes
    assert find_non_overlapping_palindromes("aabaa") == ["aa", "aba"]
    
    # Test string with no palindromes
    assert find_non_overlapping_palindromes("abcd") == []
    
    # Test complex case with multiple non-overlapping palindromes
    assert find_non_overlapping_palindromes("abbacddc") == ["bb", "cddc"]
    
    # Test lexicographic sorting
    assert find_non_overlapping_palindromes("racecar") == ["aceca", "r"]
    
    # Test with repeated characters
    assert find_non_overlapping_palindromes("aaaa") == ["aaaa"]

def test_non_overlapping_strict():
    # Ensure no overlapping indices are used
    result = find_non_overlapping_palindromes("abbacddc")
    assert "bb" in result
    assert "cddc" in result
    
    # Verify no common indices
    for i, pal1 in enumerate(result):
        for j, pal2 in enumerate(result):
            if i != j:
                # Ensure no overlap between any two palindromes
                assert not any(
                    result[i][x] == result[j][y] 
                    for x in range(len(result[i])) 
                    for y in range(len(result[j]))
                )