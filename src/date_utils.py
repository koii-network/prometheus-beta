from datetime import date

def get_current_date() -> str:
    """
    Returns the current date in YYYY-MM-DD format.
    
    Returns:
        str: Current date formatted as YYYY-MM-DD
    """
    return date.today().strftime("%Y-%m-%d")