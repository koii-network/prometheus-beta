def max_subarray_sum(arr):
    """
    Implements Kadane's algorithm to find the maximum sum of a contiguous subarray.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum sum of a contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check if list is empty
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize max_so_far and max_ending_here with the first element
    max_so_far = max_ending_here = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Update max_ending_here to be the maximum of current element 
        # or the sum of current element and previous max_ending_here
        max_ending_here = max(num, max_ending_here + num)
        
        # Update max_so_far if max_ending_here is larger
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far