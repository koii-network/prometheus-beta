import pytest
from src.email_validator import validate_email

def test_valid_email_addresses():
    """Test a variety of valid email addresses."""
    valid_emails = [
        'user@example.com',
        'john.doe@company.co.uk',
        'firstname+lastname@domain.com',
        'email123@domain-name.com',
        'user@subdomain.example.org'
    ]
    for email in valid_emails:
        assert validate_email(email) == True, f"Failed to validate: {email}"

def test_invalid_email_addresses():
    """Test a variety of invalid email addresses."""
    invalid_emails = [
        'invalid.email',  # Missing @
        '@missinguser.com',  # Missing username
        'user@.com',  # Missing domain name
        'user@domain',  # Missing top-level domain
        'user@domain.',  # Incomplete top-level domain
        'user name@domain.com',  # Spaces not allowed
        123,  # Non-string input
        None,  # None input
        '',  # Empty string
        'user@domain..com'  # Double dot not allowed
    ]
    for email in invalid_emails:
        assert validate_email(email) == False, f"Incorrectly validated: {email}"

def test_email_whitespace_handling():
    """Test that email validation handles whitespace correctly."""
    assert validate_email('  user@example.com  ') == True
    assert validate_email('  invalid.email  ') == False