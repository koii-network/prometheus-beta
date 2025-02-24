import pytest
from src.assert_conditions import validate_conditions, check_type, range_validator

def test_validate_conditions_pass():
    """Test that validate_conditions passes when all conditions are true."""
    validate_conditions(5 > 3, 10 == 10)

def test_validate_conditions_custom_message():
    """Test validate_conditions with a custom error message."""
    with pytest.raises(AssertionError, match="Custom error"):
        validate_conditions(5 > 10, message="Custom error")

def test_validate_conditions_fail():
    """Test that validate_conditions raises AssertionError when a condition is false."""
    with pytest.raises(AssertionError):
        validate_conditions(5 > 10)

def test_check_type_pass():
    """Test that check_type passes for correct types."""
    check_type(5, int)
    check_type("hello", str)
    check_type(5.5, (int, float))

def test_check_type_fail():
    """Test that check_type raises AssertionError for incorrect types."""
    with pytest.raises(AssertionError):
        check_type("hello", int)

def test_check_type_custom_message():
    """Test check_type with a custom error message."""
    with pytest.raises(AssertionError, match="Custom type error"):
        check_type("hello", int, message="Custom type error")

def test_range_validator_pass():
    """Test that range_validator passes for values within range."""
    range_validator(5, min_val=0, max_val=10)
    range_validator(0, min_val=0)
    range_validator(10, max_val=10)

def test_range_validator_min_fail():
    """Test that range_validator fails for values below minimum."""
    with pytest.raises(AssertionError):
        range_validator(-1, min_val=0)

def test_range_validator_max_fail():
    """Test that range_validator fails for values above maximum."""
    with pytest.raises(AssertionError):
        range_validator(11, max_val=10)

def test_range_validator_custom_message():
    """Test range_validator with a custom error message."""
    with pytest.raises(AssertionError, match="Custom range error"):
        range_validator(11, max_val=10, message="Custom range error")

def test_range_validator_no_bounds():
    """Test range_validator with no bounds specified."""
    # Should not raise any errors
    range_validator(5)
    range_validator(-5)
    range_validator(0)