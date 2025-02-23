import pytest
from src.assert_condition_checker import check_conditions

def test_check_conditions_all_pass():
    """Test that function returns True when all conditions pass"""
    result = check_conditions(
        (1 == 1, "Basic equality should pass"),
        (5 > 3, "Comparison condition should pass")
    )
    assert result is True

def test_check_conditions_single_condition():
    """Test function works with a single condition"""
    result = check_conditions((True, "Single condition"))
    assert result is True

def test_check_conditions_fail():
    """Test that function raises AssertionError on failed condition"""
    with pytest.raises(AssertionError, match="Failed condition"):
        check_conditions((1 == 2, "Failed condition"))

def test_check_conditions_multiple_failures():
    """Test multiple failing conditions"""
    with pytest.raises(AssertionError, match="First fail"):
        check_conditions(
            (1 == 2, "First fail"),
            (3 < 1, "Second fail")
        )

def test_check_conditions_type_check():
    """Test condition checking with type"""
    result = check_conditions(
        (isinstance(5, int), "Should be an integer"),
        (isinstance("test", str), "Should be a string")
    )
    assert result is True

def test_check_conditions_empty_input():
    """Test behavior with no conditions"""
    result = check_conditions()
    assert result is True