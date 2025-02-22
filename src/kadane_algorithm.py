def max_subarray_sum(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): List of integers to find maximum subarray sum
    
    Returns:
        int: Maximum sum of a contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_sum = current_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Kadane's Algorithm: either extend current subarray or start a new one
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum