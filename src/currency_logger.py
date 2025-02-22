def log_currency(number, currency='$', decimal_places=2):
    """
    Format and log a number with a currency symbol.
    
    Args:
        number (float or int): The number to be formatted
        currency (str, optional): Currency symbol. Defaults to '$'
        decimal_places (int, optional): Number of decimal places. Defaults to 2
    
    Returns:
        str: Formatted currency string
    
    Raises:
        TypeError: If number is not a numeric type
        ValueError: If decimal_places is negative
    """
    # Validate inputs
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be a numeric type")
    
    if decimal_places < 0:
        raise ValueError("Decimal places cannot be negative")
    
    # Format the number with specified currency and decimal places
    formatted_number = f"{currency}{number:,.{decimal_places}f}"
    
    # Log the formatted number (in a real-world scenario, you might use logging module)
    print(f"Logged currency: {formatted_number}")
    
    return formatted_number