import pytest
from src.longest_common_substring import find_longest_common_substring

def test_find_longest_common_substring():
    # Test case 1: Basic common substring
    assert find_longest_common_substring("hello world", "world hello") == "world"
    
    # Test case 2: No common substring
    assert find_longest_common_substring("abc", "def") == ""
    
    # Test case 3: Entire string is common
    assert find_longest_common_substring("python", "python") == "python"
    
    # Test case 4: Common substring at the beginning
    assert find_longest_common_substring("programming", "program") == "program"
    
    # Test case 5: Common substring at the end
    assert find_longest_common_substring("coding", "funny coding") == "coding"
    
    # Test case 6: Multiple possible common substrings
    assert find_longest_common_substring("abcdef", "abcxyz") == "abc"
    
    # Test case 7: Empty strings
    assert find_longest_common_substring("", "test") == ""
    assert find_longest_common_substring("test", "") == ""
    assert find_longest_common_substring("", "") == ""
    
    # Test case 8: Case-sensitive matching
    assert find_longest_common_substring("Hello", "hello") == ""
    
    # Test case 9: Long common substring
    assert find_longest_common_substring("ababcdefghijklmnop", "abcdefghijklmnopqrst") == "abcdefghijklmnop"

def test_type_handling():
    # Test invalid input types
    with pytest.raises(TypeError):
        find_longest_common_substring(123, "test")
    with pytest.raises(TypeError):
        find_longest_common_substring("test", 456)