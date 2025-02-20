import pytest
from src.phone_number_validator import validate_phone_number

def test_valid_phone_numbers():
    # Test all three valid formats
    assert validate_phone_number('(123) 456-7890') == True
    assert validate_phone_number('123-456-7890') == True
    assert validate_phone_number('123 456 7890') == True

def test_invalid_phone_numbers():
    # Test various invalid formats
    assert validate_phone_number('(123)456-7890') == False   # Missing space after parenthesis
    assert validate_phone_number('123 456-7890') == False    # Mixed format
    assert validate_phone_number('(123) 4567890') == False  # No hyphen
    assert validate_phone_number('abc-def-ghij') == False   # Non-numeric
    assert validate_phone_number('123.456.7890') == False   # Different separators
    assert validate_phone_number('') == False               # Empty string
    assert validate_phone_number('12345') == False          # Too short

def test_edge_cases():
    assert validate_phone_number('(000) 000-0000') == True  # All zeros
    assert validate_phone_number('(999) 999-9999') == True  # All nines