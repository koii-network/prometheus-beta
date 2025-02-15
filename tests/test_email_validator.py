import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats."""
    valid_emails = [
        "user@example.com",
        "first.last@example.co.uk",
        "user+tag@example.org",
        "user-name@example.net",
        "user_name@example.com",
        "123user@example.com",
        "user@subdomain.example.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "",  # Empty string
        "invalid-email",  # No @ symbol
        "@example.com",  # No username
        "user@",  # No domain
        "user@.com",  # Invalid domain
        "user@example",  # Missing top-level domain
        "user@example.",  # Incomplete top-level domain
        "user@example..com",  # Double dot in domain
        "user name@example.com",  # Spaces not allowed
        "user@example.c",  # Top-level domain too short
        "a" * 255 + "@example.com"  # Too long email
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email formats."""
    # Test case sensitivity of top-level domain
    assert validate_email("user@EXAMPLE.COM") is True
    
    # Test special characters in allowed positions
    assert validate_email("first.last+tag@example-domain.co.uk") is True
    
    # Test invalid special characters
    assert validate_email("user@exa(mple.com") is False
    assert validate_email("user@exam!ple.com") is False