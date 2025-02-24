def find_max_subarray(arr):
    """
    Find the contiguous subarray with the largest sum in an array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        list: The contiguous subarray with the largest sum
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Initialize variables
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    max_start = 0
    max_end = 0
    
    # Kadane's algorithm with tracking of subarray indices
    for end, num in enumerate(arr):
        # If current_sum becomes negative, reset start and current_sum
        if current_sum < 0:
            current_sum = num
            start = end
        else:
            current_sum += num
        
        # Update max_sum and subarray indices if current_sum is larger
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = end
    
    # Return the subarray with the largest sum
    return arr[max_start:max_end+1]