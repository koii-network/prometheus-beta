from datetime import datetime, timedelta

def calculate_timestamp_difference(timestamp1: str, timestamp2: str) -> float:
    """
    Calculate the absolute time difference between two timestamps in seconds.

    Args:
        timestamp1 (str): First timestamp in ISO format (e.g., '2023-06-15T10:30:00')
        timestamp2 (str): Second timestamp in ISO format (e.g., '2023-06-15T11:45:30')

    Returns:
        float: Absolute time difference in seconds

    Raises:
        ValueError: If timestamps are not in the correct ISO format
    """
    try:
        # Parse timestamps using datetime
        dt1 = datetime.fromisoformat(timestamp1)
        dt2 = datetime.fromisoformat(timestamp2)

        # Calculate absolute time difference
        time_diff = abs(dt2 - dt1)
        
        # Return total seconds
        return time_diff.total_seconds()
    
    except ValueError as e:
        # Raise a more descriptive error if parsing fails
        raise ValueError(f"Invalid timestamp format. Ensure timestamps are in ISO format: {e}")