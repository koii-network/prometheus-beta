def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This function uses Kadane's algorithm to find the maximum subarray sum in O(n) time complexity.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the previous subarray or starting a new subarray
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far