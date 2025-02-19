import pytest
from src.password_validator import validate_password

def test_valid_password():
    """Test a password that meets all complexity requirements"""
    assert validate_password('StrongP@ssw0rd2023!') == True

def test_too_short():
    """Test that passwords less than 12 characters are rejected"""
    assert validate_password('Short1!') == False

def test_no_uppercase():
    """Test that password without uppercase is rejected"""
    assert validate_password('lowercase1!password') == False

def test_no_lowercase():
    """Test that password without lowercase is rejected"""
    assert validate_password('UPPERCASE1!PASSWORD') == False

def test_no_digit():
    """Test that password without digit is rejected"""
    assert validate_password('NoDigitsHere!') == False

def test_no_special_character():
    """Test that password without special character is rejected"""
    assert validate_password('NoSpecialChars123') == False

def test_repeated_sequences():
    """Test that passwords with repeated sequences are rejected"""
    assert validate_password('AAAbbb1234!') == False

def test_common_words():
    """Test that passwords containing common words are rejected"""
    assert validate_password('password123!Test') == False
    assert validate_password('qwerty123!Test') == False

def test_edge_cases():
    """Test various edge cases"""
    assert validate_password('') == False
    assert validate_password('12345678901!A') == True
    assert validate_password('Very_Str0ng_P@ssw0rd!') == True

def test_mixed_complexity():
    """Test passwords with mixed complexity requirements"""
    test_cases = [
        'a1B!c2D3e4',
        'Complex_P@ssw0rd_2023',
        'S3cure_Str!ng_Example'
    ]
    for password in test_cases:
        assert validate_password(password) == True