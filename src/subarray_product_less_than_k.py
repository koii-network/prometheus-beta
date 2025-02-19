def count_subarrays_with_product_less_than_k(nums, k):
    """
    Count the number of subarrays where the product of elements is less than k.
    
    Args:
        nums (List[int]): Input array of positive integers
        k (int): Upper bound for subarray product
    
    Returns:
        int: Number of subarrays with product less than k
    
    Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - 1 <= nums[i] <= 1000
    - 1 <= k <= 10^6
    """
    if k <= 1:
        return 0
    
    count = 0
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
        count += right - left + 1
    
    return count