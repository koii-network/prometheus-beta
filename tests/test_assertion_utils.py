import pytest
from src.assertion_utils import check_conditions, validate_input

def test_check_conditions_pass():
    """Test check_conditions with passing conditions"""
    check_conditions([
        (1 == 1, "Equality check"),
        (10 > 5, "Greater than check"),
        (True, None)
    ])

def test_check_conditions_fail():
    """Test check_conditions with a failing condition"""
    with pytest.raises(AssertionError, match="Test condition failed"):
        check_conditions([
            (1 == 1, "Equality check"),
            (10 < 5, "Test condition failed")
        ])

def test_validate_input_pass():
    """Test validate_input with passing validators"""
    def is_positive(x):
        return x > 0
    
    def is_less_than_10(x):
        return x < 10
    
    assert validate_input(5, [
        (is_positive, "Must be positive"),
        (is_less_than_10, "Must be less than 10")
    ])

def test_validate_input_fail():
    """Test validate_input with a failing validator"""
    def is_positive(x):
        return x > 0
    
    with pytest.raises(AssertionError, match="Must be positive"):
        validate_input(-5, [
            (is_positive, "Must be positive")
        ])

def test_validate_input_complex():
    """Test validate_input with multiple and complex validators"""
    def is_string(x):
        return isinstance(x, str)
    
    def min_length(x):
        return len(x) >= 3
    
    def max_length(x):
        return len(x) <= 10
    
    assert validate_input("hello", [
        (is_string, "Must be a string"),
        (min_length, "Must be at least 3 characters"),
        (max_length, "Must be no more than 10 characters")
    ])

def test_validate_input_complex_fail():
    """Test validate_input with a complex failing validator"""
    def is_string(x):
        return isinstance(x, str)
    
    def min_length(x):
        return len(x) >= 3
    
    with pytest.raises(AssertionError, match="Must be at least 3 characters"):
        validate_input("hi", [
            (is_string, "Must be a string"),
            (min_length, "Must be at least 3 characters")
        ])