import pytest
from src.advanced_string_reversal import advanced_string_reversal

def test_advanced_string_reversal():
    # Test basic word reversal
    assert advanced_string_reversal("hello") == "olleh"
    assert advanced_string_reversal("world") == "dlrow"
    
    # Test palindromes remain unchanged
    assert advanced_string_reversal("racecar") == "racecar"
    assert advanced_string_reversal("level") == "level"
    
    # Test integer reversal
    assert advanced_string_reversal("123") == "321"
    
    # Test mixed scenarios
    assert advanced_string_reversal("hello123") == "olleh321"
    assert advanced_string_reversal("12hello34") == "12olleh43"
    
    # Test mixed strings with spaces and punctuation
    assert advanced_string_reversal("hello world 123") == "olleh dlrow 321"
    assert advanced_string_reversal("hello, world! 42") == "olleh, dlrow! 24"
    
    # Test palindromic words in a mixed string
    assert advanced_string_reversal("level hello 123") == "level olleh 321"
    
    # Test empty string
    assert advanced_string_reversal("") == ""
    
    # Test string with special characters
    assert advanced_string_reversal("hello@123") == "olleh@321"