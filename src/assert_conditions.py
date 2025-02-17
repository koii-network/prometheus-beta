def validate_conditions(*conditions, message=None):
    """
    Validate multiple conditions using assert statements.
    
    Args:
        *conditions: Variable number of conditions to check
        message (str, optional): Custom error message to display if any condition fails
    
    Raises:
        AssertionError: If any condition is False
    """
    for condition in conditions:
        assert condition, message or "One of the conditions failed"
    return True