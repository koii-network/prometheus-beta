import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test valid email addresses"""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user+tag@example.com",
        "user-name@example.co.uk",
        "user123@example.org",
        "user.name+tag@example-domain.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test invalid email addresses"""
    invalid_emails = [
        "",  # Empty string
        None,  # None value
        "invalid.email",  # Missing @ symbol
        "invalid@email",  # Missing domain extension
        "invalid@.com",  # Invalid domain
        "invalid@domain.",  # Incomplete domain
        "multiple@@at.com",  # Multiple @ symbols
        "spaces in@email.com",  # Spaces not allowed
        "no_domain@",  # No domain
        "@no_local.com",  # No local part
        "very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_long_email@example.com"  # Too long email
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email scenarios"""
    edge_cases = [
        "a@b.co",  # Shortest possible valid email
        "user@domain.a",  # Short TLD
        "user@domain.museum"  # Longer TLD
    ]
    for email in edge_cases:
        assert validate_email(email) is True, f"{email} should be valid"