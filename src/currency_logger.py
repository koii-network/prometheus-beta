def log_currency(number, currency='$', decimal_places=2):
    """
    Format a number with a currency symbol and specified decimal places.
    
    Args:
        number (float or int): The number to be formatted
        currency (str, optional): Currency symbol to use. Defaults to '$'.
        decimal_places (int, optional): Number of decimal places to round to. Defaults to 2.
    
    Returns:
        str: Formatted currency string
    
    Raises:
        TypeError: If number is not a numeric type
        ValueError: If decimal_places is negative
    """
    # Validate inputs
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be a numeric type (int or float)")
    
    if decimal_places < 0:
        raise ValueError("Decimal places cannot be negative")
    
    # Round the number to specified decimal places
    rounded_number = round(number, decimal_places)
    
    # Format the number with comma separators and specified decimal places
    return f"{currency}{rounded_number:,.{decimal_places}f}"