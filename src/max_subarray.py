def max_subarray_sum(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of a contiguous subarray.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize maximum sum and current sum
    max_sum = current_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Choose between extending current subarray or starting a new one
        current_sum = max(num, current_sum + num)
        
        # Update maximum sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum