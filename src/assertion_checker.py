def check_conditions(values, min_value=0, max_value=100):
    """
    Check conditions on a list of values using assertions.
    
    Args:
        values (list): A list of numeric values to check
        min_value (int, optional): Minimum allowed value. Defaults to 0.
        max_value (int, optional): Maximum allowed value. Defaults to 100.
    
    Returns:
        bool: True if all conditions are met
    
    Raises:
        AssertionError: If any conditions are not met
    """
    # Assert that input is a list
    assert isinstance(values, list), "Input must be a list"
    
    # Assert that the list is not empty
    assert len(values) > 0, "List cannot be empty"
    
    # Check each value meets the conditions
    for value in values:
        # Assert that each value is numeric
        assert isinstance(value, (int, float)), f"Invalid type: {type(value)}. All values must be numeric"
        
        # Assert value is within the specified range
        assert min_value <= value <= max_value, f"Value {value} is out of range [{min_value}, {max_value}]"
    
    return True