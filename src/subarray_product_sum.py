def count_subarrays_product_less_than_k(nums, k):
    """
    Count the number of subarrays with product less than k.
    
    Args:
        nums (list[int]): Input array of positive integers
        k (int): Upper bound for subarray product
    
    Returns:
        int: Total number of subarrays with product less than k
    
    Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - 1 <= nums[i] <= 1000
    - 1 <= k <= 10^6
    """
    # Handle edge cases
    if k <= 1:
        return 0
    
    total_subarrays = 0
    left = 0
    current_product = 1
    
    for right in range(len(nums)):
        # Expand the window by including the current element
        current_product *= nums[right]
        
        # Shrink the window if product exceeds k
        while current_product >= k and left <= right:
            current_product //= nums[left]
            left += 1
        
        # Count subarrays ending at current right index
        total_subarrays += right - left + 1
    
    return total_subarrays