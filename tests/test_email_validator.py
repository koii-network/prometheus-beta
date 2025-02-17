import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats"""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user_name@example.co.uk",
        "user123@example-domain.com",
        "first.last@company.org"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats"""
    invalid_emails = [
        "",  # Empty string
        "   ",  # Whitespace
        "invalid.email",  # No @ symbol
        "@missing.username",  # Missing username
        "user@.com",  # Invalid domain
        "user@domain",  # Missing top-level domain
        "user@domain..com",  # Consecutive dots
        "user@domain.c",  # Too short top-level domain
        "user@domain.toolong",  # Too long top-level domain
        "user..name@example.com",  # Consecutive dots in username
        "user@domain.-com",  # Special character at domain start/end
        123  # Non-string input
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case scenarios"""
    # Whitespace around email
    assert validate_email("  user@example.com  ") is True
    
    # Case sensitivity of username
    assert validate_email("User.Name@Example.com") is True
    
    # Special characters in appropriate places
    assert validate_email("user.name+tag@example.com") is True
    assert validate_email("user-name@example-domain.com") is True