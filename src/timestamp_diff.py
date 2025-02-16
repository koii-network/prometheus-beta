from datetime import datetime

def calculate_timestamp_difference(timestamp1, timestamp2, format='%Y-%m-%d %H:%M:%S'):
    """
    Calculate the time difference between two timestamps.
    
    Args:
        timestamp1 (str): First timestamp string
        timestamp2 (str): Second timestamp string
        format (str, optional): Timestamp format. Defaults to '%Y-%m-%d %H:%M:%S'
    
    Returns:
        dict: A dictionary containing the time difference in various units
    
    Raises:
        ValueError: If timestamps cannot be parsed with the given format
    """
    try:
        # Parse timestamps
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)
        
        # Calculate absolute time difference
        time_diff = abs(dt2 - dt1)
        
        # Return dictionary with different time representations
        return {
            'total_seconds': time_diff.total_seconds(),
            'days': time_diff.days,
            'hours': time_diff.total_seconds() / 3600,
            'minutes': time_diff.total_seconds() / 60,
            'microseconds': time_diff.microseconds
        }
    except ValueError as e:
        raise ValueError(f"Error parsing timestamps: {e}. Please ensure timestamps match the format: {format}")