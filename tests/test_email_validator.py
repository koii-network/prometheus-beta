import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from email_validator import validate_email

def test_valid_emails():
    """Test various valid email formats"""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user-name@example.com",
        "user_name@example.co.uk",
        "user123@example.org",
        "firstname.lastname@example.com",
    ]
    for email in valid_emails:
        assert validate_email(email) == True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats"""
    invalid_emails = [
        # Empty strings
        "",
        None,
        # Missing @ symbol
        "userexample.com",
        # No domain
        "user@",
        # No username
        "@example.com",
        # Invalid characters
        "user!@example.com", 
        "user@example!.com",
        # Consecutive dots
        "user..name@example.com",
        # Starts or ends with dot
        ".user@example.com",
        "user.@example.com",
        # Invalid TLD
        "user@example.c",
        # Too long
        "a" * 255 + "@example.com",
        # Too short
        "a@b.c",
    ]
    for email in invalid_emails:
        assert validate_email(email) == False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case scenarios"""
    # Emails with complex but valid formats
    complex_valid_emails = [
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
    ]
    for email in complex_valid_emails:
        assert validate_email(email) == True, f"{email} should be valid"

    # Emails with tricky but invalid formats
    complex_invalid_emails = [
        "email@-example.com",  # starts with hyphen
        "email@example..com",  # consecutive dots in domain
    ]
    for email in complex_invalid_emails:
        assert validate_email(email) == False, f"{email} should be invalid"