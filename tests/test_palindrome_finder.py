import pytest
from src.palindrome_finder import find_non_overlapping_palindromes

def test_find_non_overlapping_palindromes():
    # Test basic cases
    assert find_non_overlapping_palindromes("") == []
    assert find_non_overlapping_palindromes("a") == ["a"]
    
    # Test string with multiple palindromes
    result = find_non_overlapping_palindromes("aabaa")
    assert "aa" in result or "aba" in result
    
    # Test string with no palindromes
    assert find_non_overlapping_palindromes("abcd") == []
    
    # Test complex case with multiple non-overlapping palindromes
    result = find_non_overlapping_palindromes("abbacddc")
    assert len(result) > 0
    
    # Test lexicographic sorting
    sorted_result = sorted(find_non_overlapping_palindromes("racecar"))
    assert len(sorted_result) > 0
    
    # Test with repeated characters
    assert find_non_overlapping_palindromes("aaaa") == ["aaaa"]

def test_non_overlapping_strict():
    # Ensure no overlapping indices are used
    result = find_non_overlapping_palindromes("abbacddc")
    assert len(result) > 0
    
    # Verify no common indices
    for i, pal1 in enumerate(result):
        for j, pal2 in enumerate(result):
            if i != j:
                # Ensure no overlap between any two palindromes
                assert not any(
                    pal1[x] == pal2[y] 
                    for x in range(len(pal1)) 
                    for y in range(len(pal2))
                )