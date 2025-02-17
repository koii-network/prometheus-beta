def max_subarray_sum(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_so_far = float('-inf')  # Maximum sum found so far
    max_ending_here = 0  # Maximum sum ending at current position
    
    # Iterate through the array using Kadane's Algorithm
    for num in arr:
        # Choose between extending the previous subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the maximum sum if necessary
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far