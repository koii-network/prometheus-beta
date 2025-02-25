from datetime import date

def get_current_date_formatted() -> str:
    """
    Returns the current date in YYYY-MM-DD format.
    
    Returns:
        str: Current date as a string in YYYY-MM-DD format
    """
    return date.today().strftime("%Y-%m-%d")