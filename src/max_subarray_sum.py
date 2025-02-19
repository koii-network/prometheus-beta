def max_subarray_sum(nums, k):
    """
    Returns the maximum sum of a subarray of length 'k' within a given list of integers.
    
    Args:
        nums (list): A list of integers
        k (int): Length of the subarray
    
    Returns:
        list: A list containing the maximum subarray sum, or an empty list if k > len(nums)
    """
    if k > len(nums):
        return []
    
    # Initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(nums)):
        # Remove first element of previous window and add next element
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return [max_sum]