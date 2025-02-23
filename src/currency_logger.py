def log_currency(number, currency='$', decimal_places=2):
    """
    Format and log a number with a specified currency symbol.

    Args:
        number (int, float): The number to format and log
        currency (str, optional): Currency symbol to use. Defaults to '$'.
        decimal_places (int, optional): Number of decimal places to round to. Defaults to 2.

    Returns:
        str: Formatted currency string

    Raises:
        TypeError: If number is not a valid numeric type
        ValueError: If decimal places is negative
    """
    # Validate inputs
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be a numeric type (int or float)")
    
    if decimal_places < 0:
        raise ValueError("Decimal places cannot be negative")

    # Round the number to specified decimal places
    rounded_number = round(number, decimal_places)

    # Format the number with currency symbol
    formatted_number = f"{currency}{rounded_number:,.{decimal_places}f}"
    
    # Log the formatted number (using print for demonstration)
    print(formatted_number)
    
    return formatted_number