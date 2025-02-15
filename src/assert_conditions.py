def check_conditions(*conditions):
    """
    Validate multiple conditions using assertions.
    
    Args:
        *conditions (tuple): A variable number of condition tuples.
                             Each tuple should be in the format (condition, error_message)
    
    Raises:
        AssertionError: If any of the conditions are not met
    
    Example:
        check_conditions(
            (x > 0, "x must be positive"),
            (y < 10, "y must be less than 10")
        )
    """
    for condition, error_message in conditions:
        assert condition, error_message

def validate_input(value, condition, error_message):
    """
    Validate a single input against a specific condition.
    
    Args:
        value: The input value to validate
        condition (callable): A function that returns True or False
        error_message (str): Message to display if condition is not met
    
    Raises:
        AssertionError: If the condition is not met
    
    Example:
        validate_input(5, lambda x: x > 0, "Value must be positive")
    """
    assert condition(value), error_message