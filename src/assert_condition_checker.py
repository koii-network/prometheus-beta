def check_conditions(*conditions):
    """
    A function that uses assertions to check multiple conditions.
    
    Args:
        *conditions: Variable number of conditions to check.
                     Each condition should be a tuple of (condition, error_message)
    
    Raises:
        AssertionError: If any condition evaluates to False
    """
    for condition, error_message in conditions:
        assert condition, error_message
    return True