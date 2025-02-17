def check_conditions(*conditions):
    """
    Check multiple conditions using assertions.
    
    Args:
        *conditions (tuple): A variable number of tuples, where each tuple contains:
            - A condition to check (boolean expression)
            - An optional error message to display if the condition is False
    
    Raises:
        AssertionError: If any of the conditions evaluate to False
    """
    for condition in conditions:
        # Support both 2-tuple (condition, message) and 1-tuple (condition,) formats
        if len(condition) == 2:
            assert condition[0], condition[1]
        elif len(condition) == 1:
            assert condition[0]
        else:
            raise ValueError("Invalid condition format. Use (condition, message) or (condition,)")
    
    return True  # Return True if all conditions pass