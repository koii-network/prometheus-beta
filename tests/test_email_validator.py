import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email addresses."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user+tag@example.com",
        "user123@example.org",
        "first.last@example.com",
        "user@subdomain.example.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        # Empty or non-string inputs
        "",
        None,
        123,
        # Missing parts
        "@example.com",
        "user@",
        "@",
        # Invalid characters
        "user@example",  # Missing TLD
        "user@.com",
        "user@@example.com",
        "user@example..com",
        # Extremely long email
        ("a" * 250) + "@example.com",
        # Invalid domains
        "user@example",
        "user@example.c"
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test specific edge cases for email validation."""
    # Test emails with complex but valid formats
    edge_case_emails = [
        "user.name+tag@example.co.uk",
        "user-name@example.com",
        "user_name@example.com"
    ]
    for email in edge_case_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_email_length():
    """Test email length constraints."""
    # Test maximum allowed email length with reasonable domain
    long_but_valid_email = "a@" + ("b" * 60) + ".example.com"
    assert validate_email(long_but_valid_email) is True
    
    # Test email exceeding maximum length
    too_long_email = f"{'a' * 200}@{'b' * 200}.com"
    assert validate_email(too_long_email) is False