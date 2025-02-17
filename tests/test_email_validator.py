import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email formats"""
    valid_emails = [
        'user@example.com',
        'john.doe@example.co.uk',
        'user123@domain.org',
        'user+tag@example.net',
        'user-name@domain.com'
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats"""
    invalid_emails = [
        '',  # Empty string
        '   ',  # Whitespace
        'invalid-email',  # Missing @
        'user@',  # Missing domain
        '@domain.com',  # Missing local part
        'user@domain',  # Missing top-level domain
        'user@.com',  # Invalid domain
        123,  # Non-string input
        None  # None input
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_email_edge_cases():
    """Test edge cases and boundary conditions"""
    # Test whitespace handling
    assert validate_email('  user@example.com  ') is True
    assert validate_email('user@example.com   ') is True
    assert validate_email('   user@example.com') is True