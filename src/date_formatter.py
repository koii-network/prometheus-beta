from datetime import date

def get_current_date_formatted() -> str:
    """
    Returns the current date in YYYY-MM-DD format.

    Returns:
        str: Current date formatted as a string in YYYY-MM-DD format.
    
    Example:
        >>> get_current_date_formatted()
        '2023-06-15'
    """
    return date.today().strftime('%Y-%m-%d')