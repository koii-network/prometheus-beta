from datetime import datetime

def convert_timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date string.
    
    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)
    
    Returns:
        str: Formatted date string in the format 'Month Day, Year' (e.g., 'January 15, 2023')
    
    Raises:
        ValueError: If timestamp is not a valid number
        TypeError: If timestamp is not an int or float
    """
    # Validate input type
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be an integer or float")
    
    try:
        # Convert timestamp to datetime object
        date_obj = datetime.fromtimestamp(timestamp)
        
        # Format the date in a human-readable way
        return date_obj.strftime("%B %d, %Y")
    except (ValueError, OverflowError):
        raise ValueError("Invalid timestamp value")