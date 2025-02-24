import pytest
from src.phone_validator import validate_phone_number

def test_valid_phone_number_formats():
    """Test valid phone number formats"""
    # Test format 1: (123) 456-7890
    assert validate_phone_number('(123) 456-7890') == True
    
    # Test format 2: 123-456-7890
    assert validate_phone_number('123-456-7890') == True
    
    # Test format 3: 123 456 7890
    assert validate_phone_number('123 456 7890') == True

def test_invalid_phone_number_formats():
    """Test invalid phone number formats"""
    # Test various invalid formats
    assert validate_phone_number('123.456.7890') == False  # Dot separators
    assert validate_phone_number('1234567890') == False  # No separators
    assert validate_phone_number('(123)456-7890') == False  # No space after parenthesis
    assert validate_phone_number('(123) 456 7890') == False  # Mixed separators
    assert validate_phone_number('(12) 456-7890') == False  # Wrong area code length
    assert validate_phone_number('(123) 45-6789') == False  # Wrong group lengths

def test_edge_cases():
    """Test edge cases"""
    # Test empty string
    assert validate_phone_number('') == False
    
    # Test with leading/trailing whitespace
    assert validate_phone_number('  (123) 456-7890  ') == True
    assert validate_phone_number('  123-456-7890  ') == True
    assert validate_phone_number('  123 456 7890  ') == True
    
    # Test with non-string input
    with pytest.raises(AttributeError):
        validate_phone_number(12345678901)
        validate_phone_number(None)