from typing import List, Tuple

def max_non_overlapping_intervals(intervals: List[Tuple[int, int]]) -> int:
    """
    Find the maximum number of non-overlapping intervals.
    
    Args:
        intervals (List[Tuple[int, int]]): A list of intervals, where each interval 
                                           is represented as a tuple (start, end).
    
    Returns:
        int: The maximum number of non-overlapping intervals that can be scheduled.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    
    Raises:
        ValueError: If intervals contain invalid ranges (end < start)
    """
    # Validate input
    if not intervals:
        return 0
    
    # Check for invalid intervals
    for start, end in intervals:
        if end < start:
            raise ValueError(f"Invalid interval: start {start} must be <= end {end}")
    
    # Sort intervals by end time 
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    count = 0
    last_end_time = float('-inf')
    
    for start, end in sorted_intervals:
        # If this interval starts after the last scheduled interval ends
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count