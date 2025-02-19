def find_max_sum_subarray(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm to find maximum sum subarray
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_max = max(num, current_max + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far