from datetime import datetime

def convert_timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date format.
    
    Args:
        timestamp (int or float): A Unix timestamp (seconds since epoch)
    
    Returns:
        str: A human-readable date string in the format "Month Day, Year at Hour:Minute AM/PM"
    
    Raises:
        ValueError: If the timestamp is not a number
        TypeError: If the timestamp is not a valid Unix timestamp
    """
    try:
        # Convert timestamp to float to handle both int and float
        timestamp_float = float(timestamp)
        
        # Convert timestamp to datetime object
        date_obj = datetime.fromtimestamp(timestamp_float)
        
        # Format the date in a human-readable way
        return date_obj.strftime("%B %d, %Y at %I:%M %p")
    
    except ValueError:
        raise ValueError("Timestamp must be a valid number")
    except OverflowError:
        raise TypeError("Timestamp is not a valid Unix timestamp")