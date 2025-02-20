import pytest
from src.phone_validator import validate_phone_number

def test_valid_phone_numbers():
    # Test all three valid formats
    assert validate_phone_number('(123) 456-7890') == True
    assert validate_phone_number('123-456-7890') == True
    assert validate_phone_number('123 456 7890') == True

def test_invalid_phone_numbers():
    # Test various invalid formats
    assert validate_phone_number('1234567890') == False  # No separators
    assert validate_phone_number('(123)456-7890') == False  # Missing space after parenthesis
    assert validate_phone_number('(123) 456 7890') == False  # Mixed separators
    assert validate_phone_number('(123) 45-67890') == False  # Wrong group sizes
    assert validate_phone_number('(1234) 456-7890') == False  # Too many digits in area code
    assert validate_phone_number('') == False  # Empty string
    assert validate_phone_number('abc-def-ghij') == False  # Non-numeric characters
    assert validate_phone_number('123 4567 890') == False  # Incorrect spacing