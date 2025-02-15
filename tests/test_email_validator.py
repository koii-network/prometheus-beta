import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats"""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user_name@example.co.uk",
        "user123@example-domain.com",
        "firstname.lastname@domain.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats"""
    invalid_emails = [
        "invalid.email",  # Missing @
        "@missingusername.com",  # Missing username
        "user@.com",  # Missing domain name
        "user@domain",  # Missing top-level domain
        "user@domain.",  # Incomplete top-level domain
        "",  # Empty string
        "   ",  # Whitespace
        "user@domain@domain.com",  # Multiple @ symbols
        "user name@domain.com",  # Spaces in username
        "user@domain..com"  # Double dots
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case inputs"""
    assert validate_email(None) is False
    assert validate_email(123) is False
    assert validate_email("") is False