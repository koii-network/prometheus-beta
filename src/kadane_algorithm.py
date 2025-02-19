def max_subarray_sum(arr):
    """
    Implements Kadane's algorithm to find the maximum sum of a contiguous subarray.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum sum of a contiguous subarray.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the input list is empty.
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm implementation
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the existing subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum sum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far