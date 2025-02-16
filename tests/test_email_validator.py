import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats."""
    valid_emails = [
        'user@example.com',
        'john.doe@company.co.uk',
        'jane_doe123@domain.org',
        'firstname-lastname@domain.net'
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"Failed to validate: {email}"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        'invalid.email',  # Missing @ symbol
        '@missingusername.com',  # Missing username
        'user@.com',  # Missing domain
        'user@domain',  # Missing top-level domain
        'user@domain.c',  # Too short top-level domain
        'user@domain.toolongdomain',  # Too long top-level domain
        123,  # Non-string input
        None,  # None input
        '',  # Empty string
        'user@domain@domain.com'  # Multiple @ symbols
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"Incorrectly validated: {email}"

def test_email_case_sensitivity():
    """Test case sensitivity of valid emails."""
    mixed_case_emails = [
        'User@Example.Com',
        'JOHN.DOE@COMPANY.CO.UK',
        'jane_Doe123@Domain.org'
    ]
    for email in mixed_case_emails:
        assert validate_email(email) is True, f"Failed to validate case-sensitive email: {email}"