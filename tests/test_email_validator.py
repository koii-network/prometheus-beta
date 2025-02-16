import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email formats"""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@domain.net",
        "first.last@domain.org",
        "user+tag@example.com"
    ]
    
    for email in valid_emails:
        assert validate_email(email) == True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats"""
    invalid_emails = [
        "",  # Empty string
        "invalid-email",  # No @ symbol
        "user@",  # No domain
        "@domain.com",  # No username
        "user@domain",  # No top-level domain
        "user@domain.",  # Incomplete domain
        "user@.com",  # Invalid domain
        123,  # Non-string input
        None  # None input
    ]
    
    for email in invalid_emails:
        assert validate_email(email) == False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    # Test email with max allowed top-level domain length
    assert validate_email("user@domain.info") == True
    
    # Test email with min allowed top-level domain length
    assert validate_email("user@domain.io") == True
    
    # Test email with top-level domain longer than 4 characters
    assert validate_email("user@domain.pizza") == False
    
    # Test very long but valid email
    long_valid_email = "a" * 64 + "@domain.com"
    assert validate_email(long_valid_email) == True