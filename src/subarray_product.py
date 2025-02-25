def count_subarrays_with_product_less_than_k(nums, k):
    """
    Count the number of subarrays in nums with a product less than k.
    
    Args:
        nums (List[int]): Input array of positive integers
        k (int): Maximum product threshold
    
    Returns:
        int: Number of subarrays with product less than k
    
    Raises:
        ValueError: If k is less than 1 or if nums contains non-positive integers
    """
    # Input validation
    if k < 1:
        raise ValueError("k must be a positive integer")
    
    if any(num <= 0 for num in nums):
        raise ValueError("All numbers in the array must be positive integers")
    
    # If k is 1, no subarray can have a product less than k
    if k == 1:
        return 0
    
    # Use sliding window technique
    total_count = 0
    left = 0
    curr_product = 1
    
    for right in range(len(nums)):
        # Expand the window by including the current element
        curr_product *= nums[right]
        
        # Shrink the window from the left if product exceeds k
        while curr_product >= k and left <= right:
            curr_product //= nums[left]
            left += 1
        
        # Count subarrays ending at the current right index
        # All subarrays between left and right (inclusive) have product less than k
        total_count += max(0, right - left + 1)
    
    return total_count