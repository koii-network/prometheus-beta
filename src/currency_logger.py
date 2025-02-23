import logging
from typing import Union

def log_formatted_currency(amount: Union[int, float], 
                            currency: str = 'USD', 
                            log_level: int = logging.INFO) -> str:
    """
    Log a number with a formatted currency symbol and return the formatted string.
    
    Args:
        amount (Union[int, float]): The monetary amount to log
        currency (str, optional): Currency symbol. Defaults to 'USD'.
        log_level (int, optional): Logging level. Defaults to logging.INFO.
    
    Returns:
        str: Formatted currency string
    
    Raises:
        ValueError: If amount is negative or if currency is empty
        TypeError: If amount is not a number
    """
    # Validate inputs
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    if not currency or not isinstance(currency, str):
        raise ValueError("Currency must be a non-empty string")
    
    # Currency symbol mapping (extended for multiple currencies)
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥',
        'CAD': 'CA$',
        'AUD': 'A$',
        'CHF': 'CHF',
        'CNY': '¥',
        'default': ''
    }
    
    # Get the appropriate currency symbol
    symbol = currency_symbols.get(currency.upper(), currency_symbols['default'])
    
    # Format the number with two decimal places
    formatted_amount = f"{symbol}{amount:.2f}"
    
    # Log the formatted amount
    logger = logging.getLogger(__name__)
    logger.log(log_level, formatted_amount)
    
    return formatted_amount