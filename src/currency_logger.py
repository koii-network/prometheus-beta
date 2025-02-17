import logging

def format_currency(number, currency_symbol='$', locale='en_US'):
    """
    Format a number with a currency symbol and logging.
    
    Args:
        number (float or int): The number to be formatted and logged
        currency_symbol (str, optional): Currency symbol to use. Defaults to '$'
        locale (str, optional): Locale for formatting. Defaults to 'en_US'
    
    Returns:
        str: Formatted currency string
    
    Raises:
        TypeError: If number is not a numeric type
        ValueError: If number is negative
    """
    # Validate input
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a numeric value")
    
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    # Format the number with comma separators and two decimal places
    formatted_number = f"{number:,.2f}"
    
    # Create currency string
    currency_string = f"{currency_symbol}{formatted_number}"
    
    # Log the formatted currency
    logging.info(f"Logged currency: {currency_string}")
    
    return currency_string