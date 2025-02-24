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
    
    selected_intervals = []
    
    for interval in sorted_intervals:
        # If the current interval does not overlap with the last selected interval
        if not selected_intervals or interval[0] >= selected_intervals[-1][1]:
            selected_intervals.append(interval)
        # If current interval is completely contained within another, skip it
        elif selected_intervals and interval[0] >= selected_intervals[-1][0] and interval[1] <= selected_intervals[-1][1]:
            continue
    
    return len(selected_intervals)