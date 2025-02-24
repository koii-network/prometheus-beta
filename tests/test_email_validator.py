import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@example.org",
        "user+tag@example.net",
        "first.last@example.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "",  # Empty string
        "invalid_email",  # No @ symbol
        "user@",  # No domain
        "@example.com",  # No local part
        "user@example",  # No top-level domain
        "user@.com",  # Invalid domain
        "user@example..com",  # Double dot in domain
        "a" * 65 + "@example.com",  # Local part too long
        "user@example.com" * 3,  # Total length too long
        123,  # Non-string input
        None  # None input
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email formats."""
    edge_case_emails = [
        "user-name@example.com",
        "user_name@example.com",
        "user.name@example.com",
        "user+tag@example.com"
    ]
    for email in edge_case_emails:
        assert validate_email(email) is True, f"{email} should be valid"