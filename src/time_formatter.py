from datetime import datetime

def get_current_time_formatted() -> str:
    """
    Returns the current time in HH:MM:SS format.
    
    Returns:
        str: Current time as a string in HH:MM:SS format
    """
    return datetime.now().strftime("%H:%M:%S")