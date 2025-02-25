def find_max_subarray_sum(arr):
    """
    Find the contiguous subarray with the largest sum in the given array.
    
    Args:
        arr (list): A list of integers to search for the maximum subarray sum.
    
    Returns:
        list: A list containing the contiguous subarray with the largest sum.
        
    Raises:
        ValueError: If the input array is empty.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
        >>> find_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        [4, -1, 2, 1]
        >>> find_max_subarray_sum([1])
        [1]
    """
    # Handle empty array
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # If array has only one element, return that element
    if len(arr) == 1:
        return arr
    
    # Special case for arrays with all negative numbers
    max_elem = max(arr)
    if max_elem < 0:
        return [max_elem]
    
    # Initialize variables for Kadane's algorithm
    max_sum = 0
    current_sum = 0
    start = 0
    max_start = 0
    max_end = 0
    
    # Iterate through the array
    for end in range(len(arr)):
        # Add current element to sum
        current_sum += arr[end]
        
        # If current sum becomes greater than max sum, update max sum and indices
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = end + 1
        
        # Special handling for zero sum and maximum elements
        if current_sum == max_sum and arr[end] > 0:
            max_start = start
            max_end = end + 1
        
        # If current sum becomes negative, reset start and current sum
        if current_sum < 0:
            current_sum = 0
            start = end + 1
    
    # Return the subarray with max sum
    return arr[max_start:max_end]