def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray in the given list.
    
    This function uses Kadane's algorithm to find the maximum sum of a 
    contiguous subarray within a one-dimensional array of numbers.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_so_far = current_max = arr[0]
    
    # Iterate through the array using Kadane's algorithm
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_max = max(num, current_max + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far