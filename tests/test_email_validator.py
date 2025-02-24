import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats."""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user_name@example.com",
        "user-name@example.co.uk",
        "user123@example.org",
        "user+tag@example.net"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "",  # Empty string
        "invalid_email",  # No @ symbol
        "user@.com",  # Missing domain name
        "user@domain",  # Missing top-level domain
        "user@domain.",  # Incomplete top-level domain
        "user@domain.a",  # Too short top-level domain
        "user@domain..com",  # Double dot
        "@domain.com",  # Missing username
        "user@domain@.com",  # Multiple @ symbols
        "user name@domain.com",  # Space in username
        "user\name@domain.com",  # Backslash in username
        123  # Non-string input
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case scenarios for email validation."""
    # Test extremely long but technically valid email
    long_valid_email = "a" * 64 + "@" + "b" * 63 + "." + "c" * 63
    assert validate_email(long_valid_email) is True

    # Test email just at the length limit
    just_at_limit = "a" * 64 + "@" + "b" * 63 + "." + "c" * 2
    assert validate_email(just_at_limit) is True

    # Test email beyond length limit
    too_long_email = "a" * 65 + "@" + "b" * 64 + "." + "c" * 3
    assert validate_email(too_long_email) is False