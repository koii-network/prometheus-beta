import pytest
from src.password_validator import validate_password

def test_valid_password():
    """Test a password that meets all complexity requirements"""
    assert validate_password("StrongP@ss123") == True

def test_password_too_short():
    """Test password that is too short"""
    assert validate_password("Short1!") == False

def test_missing_uppercase():
    """Test password missing an uppercase letter"""
    assert validate_password("lowercase1!") == False

def test_missing_lowercase():
    """Test password missing a lowercase letter"""
    assert validate_password("UPPERCASE1!") == False

def test_missing_digit():
    """Test password missing a digit"""
    assert validate_password("StrongPass!") == False

def test_missing_special_character():
    """Test password missing a special character"""
    assert validate_password("StrongPass123") == False

def test_none_input():
    """Test None input"""
    assert validate_password(None) == False

def test_non_string_input():
    """Test non-string input"""
    assert validate_password(12345) == False

def test_multiple_complexity_failures():
    """Test a password failing multiple complexity checks"""
    assert validate_password("short") == False