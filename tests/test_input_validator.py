import pytest
import logging
import logging.handlers
import io
import sys

from src.input_validator import validate_and_log_input

def test_validate_and_log_input_success():
    """Test successful input validation"""
    is_valid, messages = validate_and_log_input("test", {
        'min_length': 1,
        'max_length': 10,
        'required': True
    })
    assert is_valid
    assert len(messages) == 0

def test_validate_and_log_input_required_field():
    """Test required field validation"""
    is_valid, messages = validate_and_log_input("", {
        'required': True
    })
    assert not is_valid
    assert "Input is required" in messages

def test_validate_and_log_input_min_length():
    """Test minimum length validation"""
    is_valid, messages = validate_and_log_input("a", {
        'min_length': 3
    })
    assert not is_valid
    assert "Input must be at least 3 characters long" in messages

def test_validate_and_log_input_max_length():
    """Test maximum length validation"""
    is_valid, messages = validate_and_log_input("toolongstring", {
        'max_length': 5
    })
    assert not is_valid
    assert "Input must be no more than 5 characters long" in messages

def test_validate_and_log_input_regex():
    """Test regex pattern validation"""
    # Email-like regex
    is_valid, messages = validate_and_log_input("invalid_email", {
        'regex': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    })
    assert not is_valid
    assert "Input does not match required pattern" in messages

def test_validate_and_log_input_multiple_rules():
    """Test validation with multiple rules"""
    is_valid, messages = validate_and_log_input("abc123", {
        'min_length': 2,
        'max_length': 10,  # Increased to allow 'abc123'
        'regex': r'^[a-z0-9]+$'
    })
    assert is_valid
    assert len(messages) == 0

def test_validate_and_log_input_invalid_type():
    """Test input with invalid type"""
    is_valid, messages = validate_and_log_input(123)
    assert not is_valid
    assert "Input must be a string" in messages

def test_validate_and_log_input_whitespace_handling():
    """Test handling of whitespace"""
    is_valid, messages = validate_and_log_input("   test   ", {
        'required': True
    })
    assert is_valid
    assert len(messages) == 0