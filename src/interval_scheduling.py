def max_non_overlapping_intervals(intervals):
    """
    Find the maximum number of non-overlapping intervals.
    
    Args:
        intervals (List[List[int]]): List of intervals, where each interval 
                                     is represented as [start_time, end_time]
    
    Returns:
        int: Maximum number of non-overlapping intervals that can be scheduled
    
    Raises:
        ValueError: If input is not a valid list of intervals
    """
    # Validate input
    if not intervals:
        return 0
    
    if not all(isinstance(interval, list) and len(interval) == 2 and 
               isinstance(interval[0], (int, float)) and 
               isinstance(interval[1], (int, float)) and 
               interval[0] <= interval[1] for interval in intervals):
        raise ValueError("Invalid interval format. Each interval must be [start, end] with start <= end")
    
    # Sort intervals by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    # Greedy interval scheduling
    selected_intervals = 0
    last_end_time = float('-inf')
    
    for interval in sorted_intervals:
        # If current interval starts after the last selected interval ends
        if interval[0] >= last_end_time:
            selected_intervals += 1
            last_end_time = interval[1]
    
    return selected_intervals