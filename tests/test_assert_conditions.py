import pytest
from src.assert_conditions import check_conditions, validate_input

def test_check_conditions_pass():
    """Test check_conditions with passing conditions"""
    check_conditions(
        (True, "This should pass"),
        (5 > 0, "Positive number check")
    )

def test_check_conditions_fail():
    """Test check_conditions with a failing condition"""
    with pytest.raises(AssertionError, match="Condition failed"):
        check_conditions(
            (False, "Condition failed")
        )

def test_validate_input_pass():
    """Test validate_input with passing conditions"""
    validate_input(10, lambda x: x > 0, "Must be positive")
    validate_input("hello", lambda s: len(s) > 0, "Must not be empty")

def test_validate_input_fail():
    """Test validate_input with failing conditions"""
    with pytest.raises(AssertionError, match="Must be positive"):
        validate_input(-5, lambda x: x > 0, "Must be positive")
    
    with pytest.raises(AssertionError, match="Must be less than 10"):
        validate_input(15, lambda x: x < 10, "Must be less than 10")

def test_multiple_conditions():
    """Test multiple conditions with partial failures"""
    with pytest.raises(AssertionError):
        check_conditions(
            (True, "First condition"),
            (False, "Second condition fails"),
            (True, "Third condition")
        )