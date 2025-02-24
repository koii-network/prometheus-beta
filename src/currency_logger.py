import locale
from typing import Union, Optional

def format_currency_log(
    amount: Union[int, float], 
    currency: str = 'USD', 
    precision: int = 2
) -> str:
    """
    Format a number with a currency symbol and log-friendly representation.

    Args:
        amount (int or float): The monetary amount to format
        currency (str, optional): Currency code. Defaults to 'USD'.
        precision (int, optional): Number of decimal places. Defaults to 2.

    Returns:
        str: Formatted currency string suitable for logging

    Raises:
        ValueError: If amount is negative or precision is invalid
        TypeError: If amount is not a number
    """
    # Validate inputs
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    if precision < 0:
        raise ValueError("Precision cannot be negative")

    # Currency symbol mapping
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥',
        'default': ''
    }

    # Get the appropriate currency symbol
    symbol = currency_symbols.get(currency, currency_symbols['default'])

    # Format the number with specified precision
    formatted_amount = f"{symbol}{amount:.{precision}f}"

    return formatted_amount