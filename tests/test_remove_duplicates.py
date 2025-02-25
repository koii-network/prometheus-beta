import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars():
    # Test basic functionality
    assert remove_duplicate_chars('hello') == 'helo'
    assert remove_duplicate_chars('aabbccdd') == 'abcd'
    
    # Test empty string
    assert remove_duplicate_chars('') == ''
    
    # Test string with no duplicates
    assert remove_duplicate_chars('abcdef') == 'abcdef'
    
    # Test string with mixed case
    result = remove_duplicate_chars('HelloWorld')
    assert len(result) == len(set(result.lower()))  # Ensures unique characters (case-insensitive)
    assert 'H' in result and 'e' in result and 'l' in result and 'o' in result and 'W' in result and 'r' in result and 'd' in result
    
    # Test string with spaces and special characters
    assert remove_duplicate_chars('  hello  world  ') == ' helo wrd'
    
    # Test error handling
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)