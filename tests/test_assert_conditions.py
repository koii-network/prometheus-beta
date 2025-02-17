import pytest
from src.assert_conditions import validate_conditions

def test_validate_conditions_all_true():
    """Test when all conditions are true"""
    result = validate_conditions(1 == 1, 2 > 1, 3 != 0)
    assert result is True

def test_validate_conditions_custom_message():
    """Test with a custom error message"""
    with pytest.raises(AssertionError, match="Custom error"):
        validate_conditions(1 == 2, message="Custom error")

def test_validate_conditions_all_false():
    """Test when multiple conditions are false"""
    with pytest.raises(AssertionError):
        validate_conditions(1 == 2, 3 < 1, 0 == 1)

def test_validate_conditions_mixed_conditions():
    """Test a mix of true and false conditions"""
    with pytest.raises(AssertionError):
        validate_conditions(1 == 1, 2 == 3, 3 > 2)

def test_validate_conditions_no_conditions():
    """Test with no conditions"""
    result = validate_conditions()
    assert result is True