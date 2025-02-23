import logging

def log_currency_number(number, currency='$', locale='en_US'):
    """
    Log a number with a specified currency symbol and formatting.
    
    Args:
        number (float or int): The number to be logged
        currency (str, optional): Currency symbol. Defaults to '$'.
        locale (str, optional): Locale for number formatting. Defaults to 'en_US'.
    
    Returns:
        str: Formatted currency string
    
    Raises:
        TypeError: If number is not a numeric type
        ValueError: If currency is an empty string
    """
    # Validate inputs
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be an int or float")
    
    if not currency or not isinstance(currency, str):
        raise ValueError("Currency must be a non-empty string")
    
    try:
        # Format the number with comma separators and 2 decimal places
        formatted_number = f"{currency}{number:,.2f}"
        
        # Log the formatted number
        logging.info(f"Currency Log: {formatted_number}")
        
        return formatted_number
    except Exception as e:
        logging.error(f"Error formatting currency: {e}")
        raise