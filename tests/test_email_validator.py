import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats."""
    valid_emails = [
        'user@example.com',
        'user.name@example.co.uk',
        'user+tag@example.org',
        'firstname.lastname@example.com',
        'user123@example.net'
    ]
    
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        'invalid.email',  # Missing @ symbol
        '@missingusername.com',  # Missing username
        'user@.com',  # Missing domain name
        'user@domain',  # Missing top-level domain
        'user@domain.',  # Incomplete top-level domain
        'user name@example.com',  # Spaces not allowed
        '',  # Empty string
        None,  # None is not a valid input
        123  # Non-string input
    ]
    
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email scenarios."""
    # Very long but valid email
    long_valid_email = 'a' * 64 + '@example.com'
    assert validate_email(long_valid_email) is True
    
    # Special characters in local part
    special_chars_email = 'user.name+tag@example.com'
    assert validate_email(special_chars_email) is True