def find_longest_subarray_with_diff(A, k):
    """
    Find the length of the longest subarray where the absolute difference 
    between adjacent elements is greater than or equal to k.
    
    Args:
        A (list): List of integers
        k (int): Minimum absolute difference between adjacent elements
    
    Returns:
        int: Length of the longest subarray satisfying the condition
    
    Raises:
        ValueError: If input list is empty or k is negative
    """
    # Input validation
    if not A:
        raise ValueError("Input array cannot be empty")
    if k < 0:
        raise ValueError("Difference k must be non-negative")
    
    # If array has only one element, return 1
    if len(A) == 1:
        return 1
    
    # Use sliding window technique
    max_length = 1
    start = 0
    
    for end in range(1, len(A)):
        # Check if the absolute difference meets the condition
        if abs(A[end] - A[end-1]) >= k:
            # Update max length if current window is longer
            max_length = max(max_length, end - start + 1)
        else:
            # Reset the start of the window
            start = end
    
    return max_length