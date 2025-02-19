def kadanes_algorithm(arr):
    """
    Implement Kadane's algorithm to find the maximum subarray sum.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum subarray sum.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm implementation
    max_so_far = float('-inf')  # Maximum sum found so far
    max_ending_here = 0  # Maximum sum ending at current position
    
    for num in arr:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the maximum sum found so far
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far