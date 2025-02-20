import pytest
from src.email_validator import validate_email

def test_valid_emails():
    # Test valid email formats
    valid_emails = [
        "user@example.com",
        "first.last@example.co.uk",
        "user123@domain.org",
        "user-name@domain.net",
        "user_name@domain.io"
    ]
    
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    # Test invalid email formats
    invalid_emails = [
        "invalid.email",  # Missing @
        "@missingusername.com",  # Missing username
        "user@.com",  # Invalid domain
        "user@domain",  # Missing top-level domain
        "user@domain..com",  # Consecutive dots
        "user@domain@com",  # Multiple @ symbols
        "",  # Empty string
        None,  # None type
        "a" * 65 + "@domain.com",  # Username too long
        "user@" + "a" * 255 + ".com"  # Total email too long
    ]
    
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    # Test edge cases
    edge_case_emails = [
        "user+tag@example.com",  # Plus sign in username
        "user.name@example.co",  # Two-letter top-level domain
        "user.name@example.travel"  # Long top-level domain
    ]
    
    for email in edge_case_emails:
        assert validate_email(email) is True, f"{email} should be valid"