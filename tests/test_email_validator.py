import pytest
from src.email_validator import validate_email

def test_valid_email_addresses():
    """Test various valid email address formats"""
    valid_emails = [
        "user@example.com",
        "user.name@example.co.uk",
        "user+tag@example.org",
        "user123@example-domain.com",
        "first.last@example.io"
    ]
    
    for email in valid_emails:
        assert validate_email(email) is True, f"Failed to validate valid email: {email}"

def test_invalid_email_addresses():
    """Test various invalid email address formats"""
    invalid_emails = [
        "invalid.email",
        "@missing-username.com",
        "user@.com",
        "user@domain",
        "user@domain.",
        123456,  # Non-string input
        None,
        "",
        "user@domain@invalid.com"
    ]
    
    for email in invalid_emails:
        assert validate_email(email) is False, f"Incorrectly validated invalid email: {email}"

def test_email_case_sensitivity():
    """Test email validation is case-insensitive for local part"""
    mixed_case_emails = [
        "User@Example.com",
        "USER@EXAMPLE.COM",
        "user@Example.Com"
    ]
    
    for email in mixed_case_emails:
        assert validate_email(email) is True, f"Failed to validate case-variant email: {email}"