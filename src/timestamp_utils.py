from datetime import datetime

def calculate_time_difference(timestamp1, timestamp2, format='%Y-%m-%d %H:%M:%S'):
    """
    Calculate the time difference between two timestamps.
    
    Args:
        timestamp1 (str): First timestamp string
        timestamp2 (str): Second timestamp string
        format (str, optional): Datetime format string. Defaults to '%Y-%m-%d %H:%M:%S'
    
    Returns:
        dict: A dictionary containing time difference in days, hours, minutes, and seconds
    
    Raises:
        ValueError: If timestamps cannot be parsed or are invalid
    """
    try:
        # Parse timestamps into datetime objects
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)
        
        # Calculate absolute time difference
        time_diff = abs(dt2 - dt1)
        
        # Extract components
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
            'total_seconds': int(time_diff.total_seconds())
        }
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format. {str(e)}")