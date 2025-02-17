import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email formats"""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user-name@example.co.uk",
        "user_name123@example-domain.com",
        "user+tag@example.org"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test invalid email formats"""
    invalid_emails = [
        "invalid_email",
        "user@.com",
        "@example.com",
        "user@example",
        "user@.example.com",
        "user@example..com",
        123,  # non-string input
        None,
        ""
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case scenarios"""
    # Test extremely long but valid email
    long_email = "a" * 64 + "@" + "b" * 255 + ".com"
    assert validate_email(long_email) is True

    # Test email with all allowed special characters
    special_char_email = "user.name_123+tag@example-domain.co.uk"
    assert validate_email(special_char_email) is True