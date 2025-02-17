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
    assert remove_duplicate_chars('HelloWorld') == 'Helord'
    assert remove_duplicate_chars('HelloWorld') == remove_duplicate_chars('helloworld')
    
    # Test string with spaces and special characters
    assert remove_duplicate_chars('  hello  world  ') == ' helo wrd'
    
    # Test error handling
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)