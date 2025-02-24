from typing import List, Tuple

def max_non_overlapping_intervals(intervals: List[Tuple[int, int]]) -> int:
    """
    Find the maximum number of non-overlapping intervals using the interval scheduling algorithm.
    
    Args:
        intervals (List[Tuple[int, int]]): List of intervals, where each interval 
                                           is represented as a tuple (start, end)
    
    Returns:
        int: Maximum number of non-overlapping intervals that can be selected
    
    Raises:
        ValueError: If input intervals are invalid (e.g., negative times)
    """
    # Validate input
    if not intervals:
        return 0
    
    # Check for invalid intervals
    for start, end in intervals:
        if start > end:
            raise ValueError(f"Invalid interval: start {start} is greater than end {end}")
    
    # Sort intervals by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    result = 0
    last_end_time = float('-inf')
    
    for start, end in sorted_intervals:
        # Select an interval if it starts after or at the end of the previous interval
        if start >= last_end_time:
            result += 1
            last_end_time = end
    
    return result