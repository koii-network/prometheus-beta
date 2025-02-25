import pytest
from src.remove_excessive_duplicates import remove_excessive_duplicates

def test_remove_excessive_duplicates():
    # Test cases with multiple scenarios
    assert remove_excessive_duplicates("aabbbcccc") == "aabb"
    assert remove_excessive_duplicates("abcde") == "abcde"  # No duplicates
    assert remove_excessive_duplicates("aabbccddee") == "aabbccddee"  # 2 occurrences allowed
    assert remove_excessive_duplicates("aaabbbcccddd") == "aabbccdd"
    assert remove_excessive_duplicates("") == ""  # Empty string
    
def test_remove_excessive_duplicates_edge_cases():
    # Test edge cases and error handling
    with pytest.raises(TypeError):
        remove_excessive_duplicates(123)  # Non-string input
    with pytest.raises(TypeError):
        remove_excessive_duplicates(None)  # None input
    
def test_remove_excessive_duplicates_special_chars():
    # Test with special characters and spaces
    assert remove_excessive_duplicates("aa!!bbb@@ccc") == "aa!bbc"
    assert remove_excessive_duplicates("  aaa   bbb") == "  a   b"