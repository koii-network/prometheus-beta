import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email formats."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@example-domain.com",
        "first+last@example.com",
        "user@subdomain.example.com"
    ]
    
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "",  # Empty string
        "invalid-email",  # No @ symbol
        "@missing-username.com",  # Missing username
        "user@.com",  # Missing domain
        "user@domain",  # Missing top-level domain
        "user@domain..com",  # Double dots
        "user name@example.com",  # Spaces not allowed
        "very_long_email_" + "a"*250 + "@example.com"  # Too long
    ]
    
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge cases and type checking."""
    assert validate_email(None) is False
    assert validate_email(123) is False
    assert validate_email("") is False