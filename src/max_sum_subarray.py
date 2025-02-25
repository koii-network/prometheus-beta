def find_max_sum_subarray(arr):
    """
    Find the maximum sum of a contiguous subarray within a one-dimensional array of integers.
    
    This implementation uses Kadane's algorithm to efficiently find the maximum sum subarray.
    It handles various cases including all negative numbers, mixed positive and negative numbers,
    and empty arrays.
    
    Args:
        arr (list): A list of integers to search for the maximum sum subarray.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
             Returns 0 for an empty array.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Examples:
        >>> find_max_sum_subarray([1, -2, 3, 4, -1, 5])
        11
        >>> find_max_sum_subarray([-1, -2, -3])
        -1
        >>> find_max_sum_subarray([])
        0
    """
    # Handle empty array case
    if not arr:
        return 0
    
    # Initialize variables for Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum sum if necessary
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far