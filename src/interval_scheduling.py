from typing import List, Tuple

def max_parallel_intervals(intervals: List[Tuple[int, int]]) -> int:
    """
    Find the maximum number of non-overlapping intervals that can be scheduled simultaneously.
    
    Args:
        intervals (List[Tuple[int, int]]): A list of intervals, where each interval 
                                           is represented as a tuple (start, end).
    
    Returns:
        int: The maximum number of non-overlapping intervals that can be scheduled.
    
    Raises:
        ValueError: If input intervals are invalid (e.g., end time before start time).
    
    Time Complexity: O(n log n), where n is the number of intervals
    Space Complexity: O(n)
    
    Example:
        >>> max_parallel_intervals([(1, 3), (2, 4), (3, 5), (7, 9)])
        2
    """
    # Validate input intervals
    if not intervals:
        return 0
    
    # Check for invalid intervals
    for start, end in intervals:
        if start > end:
            raise ValueError(f"Invalid interval: start {start} is greater than end {end}")
    
    # Sort intervals by start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    # Track the end times of currently scheduled intervals
    scheduled_ends = []
    max_parallel = 0
    
    for start, end in sorted_intervals:
        # Remove intervals that have ended before the current interval starts
        scheduled_ends = [e for e in scheduled_ends if e > start]
        
        # Add the current interval's end time
        scheduled_ends.append(end)
        
        # Update max parallel intervals
        max_parallel = max(max_parallel, len(scheduled_ends))
    
    return max_parallel