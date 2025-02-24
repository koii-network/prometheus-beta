def count_subarrays_with_product_less_than_k(nums, k):
    """
    Count the number of subarrays in nums where the product of all elements is less than k.
    
    Args:
        nums (List[int]): Input array of positive integers
        k (int): Maximum product threshold
    
    Returns:
        int: Total number of subarrays with product less than k
    
    Raises:
        ValueError: If k is less than 1 or input array is empty
    """
    # Input validation
    if k < 1:
        raise ValueError("k must be at least 1")
    
    if not nums:
        return 0
    
    # Use sliding window technique
    count = 0
    left = 0
    curr_product = 1
    
    for right in range(len(nums)):
        # Extend the window by multiplying with current element
        curr_product *= nums[right]
        
        # Shrink window from left if product exceeds k
        while curr_product >= k and left <= right:
            curr_product //= nums[left]
            left += 1
        
        # Add count of valid subarrays ending at right index
        count += right - left + 1
    
    return count