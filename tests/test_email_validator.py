import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email formats."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@example-domain.com",
        "first.last@example.org",
        "user+tag@example.net"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "invalid.email",  # missing @ symbol
        "@example.com",   # missing username
        "user@.com",      # missing domain
        "user@example",   # missing top-level domain
        "user@example.",  # incomplete top-level domain
        123,              # non-string input
        None,             # None input
        "user@exam ple.com",  # space in domain
        "user@example..com"   # double dot
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email formats."""
    edge_case_emails = [
        "a@b.co",         # minimal valid email
        "a" * 64 + "@example.com",  # long username
        "user@" + "a" * 255 + ".com"  # long domain
    ]
    for email in edge_case_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_characters():
    """Test emails with invalid characters."""
    invalid_char_emails = [
        "user@exam/ple.com",
        "user@exam:ple.com",
        "user@exam\ple.com"
    ]
    for email in invalid_char_emails:
        assert validate_email(email) is False, f"{email} should be invalid"