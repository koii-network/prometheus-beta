import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats."""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user+tag@example.com",
        "user-name@example.co.uk",
        "user123@example-domain.com",
        "user.name+tag@subdomain.example.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "",                     # Empty string
        None,                   # None value
        "invalid_email",        # No @ symbol
        "user@",                # No domain
        "@example.com",         # No username
        "user@.com",            # Invalid domain
        "user@example",         # No top-level domain
        "user..name@example.com", # Consecutive dots
        "user@example..com",    # Consecutive dots in domain
        "user name@example.com", # Spaces in email
        "user@exam ple.com",    # Spaces in domain
        "user@-example.com",    # Starts with hyphen
        "user@example-.com",    # Ends with hyphen
        "a" * 255 + "@example.com"  # Too long
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_non_string_input():
    """Test non-string input types."""
    non_string_inputs = [
        123,
        [],
        {},
        True,
        False
    ]
    for input_val in non_string_inputs:
        assert validate_email(input_val) is False, f"{input_val} should be invalid"

def test_international_domains():
    """Test punycode international domain names."""
    international_emails = [
        "user@xn--d1acufc.xn--p1ai"  # Punycode is valid
    ]
    for email in international_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_special_char_emails():
    """Test emails with special characters."""
    special_char_emails = [
        "user.name@example.com",
        "user+tag@example.com"
    ]
    for email in special_char_emails:
        assert validate_email(email) is True, f"{email} should be valid"