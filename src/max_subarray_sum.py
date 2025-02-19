def find_max_subarray_sum(arr):
    """
    Find the contiguous subarray with the largest sum in an array of integers.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        list: A contiguous subarray with the largest sum.
        If the input array is empty, returns an empty list.
    """
    if not arr:
        return []
    
    # Initialize variables
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    max_start = 0
    max_end = 0
    
    for end in range(len(arr)):
        # If current_sum becomes negative, reset start and current_sum
        if current_sum < 0:
            current_sum = 0
            start = end
        
        # Add current element to sum
        current_sum += arr[end]
        
        # Update max_sum and max subarray indices if needed
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = end
    
    # Return the subarray with the largest sum
    return arr[max_start:max_end+1]