import pytest
from src.phone_validation import validate_phone_number

def test_valid_phone_numbers():
    # Test the three valid formats
    assert validate_phone_number("(123) 456-7890") == True
    assert validate_phone_number("123-456-7890") == True
    assert validate_phone_number("123 456 7890") == True

def test_invalid_phone_numbers():
    # Test various invalid formats
    assert validate_phone_number("(123)456-7890") == False  # Missing space after parenthesis
    assert validate_phone_number("123 456-7890") == False  # Mixed separators
    assert validate_phone_number("(123)-456-7890") == False  # Extra hyphen 
    assert validate_phone_number("1234567890") == False  # No separators
    assert validate_phone_number("123.456.7890") == False  # Dots instead of separators
    assert validate_phone_number("(123) 45-67890") == False  # Wrong segment lengths
    assert validate_phone_number("(12) 456-7890") == False  # Incorrect area code length
    assert validate_phone_number("") == False  # Empty string

def test_edge_cases():
    # Test edge cases and type handling
    assert validate_phone_number(" (123) 456-7890 ") == False  # Whitespace padding
    with pytest.raises(TypeError):
        validate_phone_number(1234567890)  # Non-string input