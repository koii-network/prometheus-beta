import pytest
from src.password_validator import validate_password

def test_valid_password():
    """Test that a password meeting all requirements is valid."""
    assert validate_password("StrongP@ss123") == True

def test_password_too_short():
    """Test that passwords less than 8 characters are invalid."""
    assert validate_password("Short1!") == False

def test_missing_uppercase():
    """Test that passwords without uppercase letters are invalid."""
    assert validate_password("lowercase1!") == False

def test_missing_lowercase():
    """Test that passwords without lowercase letters are invalid."""
    assert validate_password("UPPERCASE1!") == False

def test_missing_digit():
    """Test that passwords without digits are invalid."""
    assert validate_password("NoDigitPass!") == False

def test_missing_special_character():
    """Test that passwords without special characters are invalid."""
    assert validate_password("NoSpecialChar123") == False

def test_none_input():
    """Test that None input is invalid."""
    assert validate_password(None) == False

def test_non_string_input():
    """Test that non-string inputs are invalid."""
    assert validate_password(12345) == False

def test_complex_valid_passwords():
    """Test multiple valid password variations."""
    valid_passwords = [
        "Complex1!Pass",
        "Another2@Test",
        "S3cure!Password",
        "1234ABcd!@#$"
    ]
    for password in valid_passwords:
        assert validate_password(password) == True

def test_complex_invalid_passwords():
    """Test multiple invalid password variations."""
    invalid_passwords = [
        "",  # empty string
        "short",  # too short
        "NOLOWERCASE123!",  # no lowercase
        "nouppercase123!",  # no uppercase
        "NoDigits!Pass",  # no digits
        "NoSpecialPass123"  # no special characters
    ]
    for password in invalid_passwords:
        assert validate_password(password) == False