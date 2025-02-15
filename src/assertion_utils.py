def check_conditions(conditions):
    """
    Check multiple conditions using assertions.
    
    Args:
        conditions (list): A list of tuples, where each tuple contains:
            - A condition to check (any expression that evaluates to True/False)
            - An optional error message to display if the condition fails
    
    Raises:
        AssertionError: If any of the conditions fail
    """
    for condition, message in conditions:
        # If no custom message is provided, use a default
        if message is None:
            message = "Assertion failed"
        
        # Check the condition and raise AssertionError with the message if it fails
        assert condition, message

def validate_input(input_value, validators):
    """
    Validate an input value against a list of validation conditions.
    
    Args:
        input_value: The value to validate
        validators (list): A list of tuples, where each tuple contains:
            - A validation function that returns True if valid, False otherwise
            - An optional error message to display if validation fails
    
    Raises:
        AssertionError: If any validation fails
    
    Returns:
        bool: True if all validations pass
    """
    for validator, message in validators:
        # If no custom message is provided, use a default
        if message is None:
            message = "Input validation failed"
        
        # Check the validator and raise AssertionError with the message if it fails
        assert validator(input_value), message
    
    return True