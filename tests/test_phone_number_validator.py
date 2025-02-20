import pytest
from src.phone_number_validator import validate_phone_number

def test_valid_phone_number_formats():
    """Test valid phone number formats"""
    valid_numbers = [
        "(123) 456-7890",  # Format 1
        "123-456-7890",    # Format 2
        "123 456 7890"     # Format 3
    ]
    
    for number in valid_numbers:
        assert validate_phone_number(number) == True, f"Failed for valid number: {number}"

def test_invalid_phone_number_formats():
    """Test invalid phone number formats"""
    invalid_numbers = [
        "1234567890",          # No separators
        "(123)456-7890",       # Missing space after parenthesis
        "123 4567890",         # Incorrect spacing
        "(123) 456-789",       # Too few digits
        "(123) 456-78901",     # Too many digits
        "abc-def-ghij",        # Non-numeric characters
        "",                    # Empty string
        "   ",                 # Whitespace
        "123.456.7890"         # Different separator
    ]
    
    for number in invalid_numbers:
        assert validate_phone_number(number) == False, f"Failed for invalid number: {number}"

def test_edge_cases():
    """Test edge cases"""
    # Ensure the function handles different types of input
    with pytest.raises(AttributeError):
        validate_phone_number(None)
    
    with pytest.raises(AttributeError):
        validate_phone_number(12345678)