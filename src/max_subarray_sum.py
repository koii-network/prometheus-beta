def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray using Kadane's algorithm.
    
    Args:
        arr (list): A list of integers 
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm to find maximum subarray sum
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if the current subarray sum is larger
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far