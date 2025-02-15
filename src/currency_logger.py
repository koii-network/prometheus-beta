def log_currency(number, currency_symbol='$', decimal_places=2):
    """
    Format a number with a currency symbol and specified decimal places.
    
    Args:
        number (float or int): The number to be formatted
        currency_symbol (str, optional): The currency symbol to use. Defaults to '$'.
        decimal_places (int, optional): Number of decimal places to display. Defaults to 2.
    
    Returns:
        str: Formatted currency string
    
    Raises:
        TypeError: If number is not a numeric type
        ValueError: If decimal_places is negative
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    if decimal_places < 0:
        raise ValueError("Decimal places cannot be negative")
    
    # Format the number with specified decimal places and currency symbol
    return f"{currency_symbol}{number:,.{decimal_places}f}"