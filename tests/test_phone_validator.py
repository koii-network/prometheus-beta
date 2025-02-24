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
    # Test invalid formats
    assert validate_phone_number('123.456.7890') == False  # Dot separator
    assert validate_phone_number('1234567890') == False  # No separators
    assert validate_phone_number('(123)456-7890') == False  # Missing space after parenthesis
    assert validate_phone_number('(123) 456 7890') == False  # Mixed separators
    assert validate_phone_number('(123) 45-67890') == False  # Incorrect grouping
    
def test_edge_cases():
    """Test edge cases"""
    # Test whitespace handling
    assert validate_phone_number(' (123) 456-7890 ') == True
    
    # Test empty string
    assert validate_phone_number('') == False
    
    # Test None input
    with pytest.raises(TypeError):
        validate_phone_number(None)
    
def test_non_numeric_characters():
    """Test phone numbers with non-numeric characters"""
    assert validate_phone_number('(abc) def-ghij') == False
    assert validate_phone_number('123-abc-defg') == False