import datetime

def get_current_time():
    """
    Return the current time in HH:MM:SS format.
    
    Returns:
        str: Current time formatted as HH:MM:SS
    """
    return datetime.datetime.now().strftime("%H:%M:%S")