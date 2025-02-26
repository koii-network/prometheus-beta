def max_subarray_sum(nums, k):
    """
    Find the maximum sum of a subarray of length k in the given list.
    
    Args:
        nums (list): List of integers
        k (int): Length of the subarray
    
    Returns:
        list: Subarray with maximum sum, or empty list if k > len(nums)
    """
    # If k is larger than the list length, return empty list
    if k > len(nums):
        return []
    
    # If k is 0 or negative, return empty list
    if k <= 0:
        return []
    
    # Initialize the first window sum
    current_window_sum = sum(nums[:k])
    max_window_sum = current_window_sum
    max_window_start = 0
    
    # Sliding window approach
    for i in range(1, len(nums) - k + 1):
        # Remove first element of previous window and add next element
        current_window_sum = current_window_sum - nums[i-1] + nums[i+k-1]
        
        # Update max sum if current window sum is larger
        if current_window_sum > max_window_sum:
            max_window_sum = current_window_sum
            max_window_start = i
    
    # Return the subarray with maximum sum
    return nums[max_window_start:max_window_start+k]