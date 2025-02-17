import pytest
from src.assert_conditions import check_conditions

def test_check_conditions_pass():
    # Test passing simple conditions
    assert check_conditions((True,), (1 == 1,)) == True

def test_check_conditions_with_messages():
    # Test conditions with custom error messages
    assert check_conditions(
        (5 > 3, "5 should be greater than 3"),
        (10 % 2 == 0, "10 should be even")
    ) == True

def test_check_conditions_fail_without_message():
    # Test that an assertion fails without a custom message
    with pytest.raises(AssertionError):
        check_conditions((False,))

def test_check_conditions_fail_with_message():
    # Test that an assertion fails with a custom message
    with pytest.raises(AssertionError, match="Custom error message"):
        check_conditions((False, "Custom error message"))

def test_check_conditions_multiple_conditions():
    # Test multiple conditions with some passing and some failing
    with pytest.raises(AssertionError):
        check_conditions(
            (True, "This should pass"),
            (False, "This should fail")
        )

def test_check_conditions_invalid_format():
    # Test invalid condition format
    with pytest.raises(ValueError):
        check_conditions((True, "message", "extra"))