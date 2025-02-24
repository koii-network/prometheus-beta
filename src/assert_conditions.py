def validate_conditions(*conditions, message=None):
    """
    Validate multiple conditions using assert statements.

    This function takes one or more conditions and optionally a custom error message.
    It checks each condition and raises an AssertionError if any condition is False.

    Args:
        *conditions (bool): One or more boolean conditions to validate
        message (str, optional): Custom error message if any condition fails. 
                                 Defaults to None.

    Raises:
        AssertionError: If any of the provided conditions are False

    Examples:
        >>> validate_conditions(5 > 3, 10 == 10)  # Passes silently
        >>> validate_conditions(5 > 3, 10 == 9)   # Raises AssertionError
    """
    # If no custom message is provided, use a generic one
    default_message = "One or more conditions failed validation"
    error_message = message or default_message

    # Check each condition
    for condition in conditions:
        assert condition, error_message

def check_type(value, expected_type, message=None):
    """
    Check if a value is of the expected type.

    Args:
        value: The value to check
        expected_type (type or tuple of types): The expected type(s)
        message (str, optional): Custom error message. Defaults to None.

    Raises:
        AssertionError: If the value is not of the expected type

    Examples:
        >>> check_type(5, int)  # Passes silently
        >>> check_type("hello", int)  # Raises AssertionError
    """
    # If no custom message is provided, create a descriptive default
    default_message = f"Expected type {expected_type}, but got {type(value)}"
    error_message = message or default_message

    # Check the type
    assert isinstance(value, expected_type), error_message

def range_validator(value, min_val=None, max_val=None, message=None):
    """
    Validate that a value is within a specified range.

    Args:
        value: The value to validate
        min_val (comparable, optional): Minimum allowed value. Defaults to None.
        max_val (comparable, optional): Maximum allowed value. Defaults to None.
        message (str, optional): Custom error message. Defaults to None.

    Raises:
        AssertionError: If the value is outside the specified range

    Examples:
        >>> range_validator(5, min_val=0, max_val=10)  # Passes silently
        >>> range_validator(15, min_val=0, max_val=10)  # Raises AssertionError
    """
    # Construct a custom error message if not provided
    if message is None:
        message_parts = []
        if min_val is not None:
            message_parts.append(f"value must be >= {min_val}")
        if max_val is not None:
            message_parts.append(f"value must be <= {max_val}")
        default_message = f"Value out of range: {' and '.join(message_parts)}"
        message = default_message

    # Check minimum value if specified
    if min_val is not None:
        assert value >= min_val, message

    # Check maximum value if specified
    if max_val is not None:
        assert value <= max_val, message