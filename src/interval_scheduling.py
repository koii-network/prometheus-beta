from typing import List, Tuple

def max_non_overlapping_intervals(intervals: List[Tuple[int, int]]) -> int:
    """
    Find the maximum number of non-overlapping intervals using a careful selection strategy.
    
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
    
    # Sort intervals first by end time, then by length (prefer shorter intervals)
    sorted_intervals = sorted(intervals, key=lambda x: (x[1], x[1] - x[0]))
    
    selected_intervals = []
    
    for interval in sorted_intervals:
        # Check if the current interval overlaps with any previously selected interval
        if not any(max(selected_start, interval[0]) < min(selected_end, interval[1]) 
                   for selected_start, selected_end in selected_intervals):
            selected_intervals.append(interval)
    
    return len(selected_intervals)