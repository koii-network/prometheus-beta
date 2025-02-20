from typing import List, Tuple

def max_non_overlapping_intervals(intervals: List[Tuple[int, int]]) -> int:
    """
    Find the maximum number of non-overlapping intervals that can be scheduled.
    
    Args:
        intervals (List[Tuple[int, int]]): List of intervals, where each interval 
                                           is a tuple (start_time, end_time)
    
    Returns:
        int: Maximum number of non-overlapping intervals that can be scheduled
    
    Raises:
        ValueError: If intervals contain invalid time ranges
    """
    # Validate input
    if not intervals:
        return 0
    
    # Check for invalid intervals
    for start, end in intervals:
        if start > end:
            raise ValueError(f"Invalid interval: start time {start} is greater than end time {end}")
    
    # Sort intervals by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    max_intervals = 0
    last_end_time = float('-inf')
    
    for start, end in sorted_intervals:
        # If current interval starts after or at the last scheduled interval's end time
        if start >= last_end_time:
            max_intervals += 1
            last_end_time = end
    
    return max_intervals