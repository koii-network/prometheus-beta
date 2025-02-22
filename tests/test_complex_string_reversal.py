import pytest
from src.complex_string_reversal import complex_string_reversal

def test_complex_string_reversal():
    # Test cases covering different scenarios
    assert complex_string_reversal("hello") == "olleh"
    assert complex_string_reversal("hello123") == "olleh321"
    assert complex_string_reversal("123hello") == "123olleh"
    assert complex_string_reversal("racecar") == "racecar"  # palindrome remains unchanged
    assert complex_string_reversal("hello world") == "olleh dlrow"
    assert complex_string_reversal("12 hello 345") == "12 olleh 543"
    assert complex_string_reversal("") == ""  # empty string
    assert complex_string_reversal("a1b2c3") == "a1b2c3"
    assert complex_string_reversal("hello123world") == "olleh321dlrow"
    
    # Additional edge cases
    assert complex_string_reversal("a") == "a"
    assert complex_string_reversal("1a2b3c") == "1a2b3c"