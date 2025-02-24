import pytest
from src.email_validator import validate_email

def test_valid_email_addresses():
    """Test various valid email addresses."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@domain.org",
        "first-last@domain.com",
        "user_name@domain.net",
        "test.email+tag@example.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_email_addresses():
    """Test various invalid email addresses."""
    invalid_emails = [
        "",  # Empty string
        "invalid.email",  # No @ symbol
        "@missingusername.com",  # Missing username
        "user@.com",  # Missing domain
        "user@domain",  # Missing top-level domain
        "user@domain..com",  # Consecutive dots
        ".user@domain.com",  # Leading dot in local part
        "user.@domain.com",  # Trailing dot in local part
        "user@.domain.com",  # Leading dot in domain
        "user@domain.com.",  # Trailing dot in domain
        "invalid@domain",  # No top-level domain
        "a"*255 + "@domain.com",  # Too long
        "user@domain@domain.com",  # Multiple @ symbols
        None,  # None input
        123,  # Non-string input
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email scenarios."""
    edge_cases = [
        "a@b.co",  # Minimum valid length
        "very" + "long"*50 + "@domain.com",  # Long but valid email
        "user+tag@very-long-domain.co.uk"
    ]
    for email in edge_cases:
        assert validate_email(email) is True, f"{email} should be valid"