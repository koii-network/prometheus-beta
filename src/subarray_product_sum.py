def count_subarrays_with_product_less_than_k(nums, k):
    """
    Calculate the number of subarrays with product less than k.
    
    Args:
        nums (List[int]): Input array of integers
        k (int): Maximum product threshold
    
    Returns:
        int: Number of subarrays with product less than k
    
    Raises:
        ValueError: If input is not a valid list or k is not a positive number
    """
    # Validate inputs
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers")
    if not isinstance(k, (int, float)) or k <= 0:
        raise ValueError("k must be a positive number")
    
    # Handle empty array case
    if not nums:
        return 0
    
    # Initialize variables
    total_subarrays = 0
    left = 0
    curr_product = 1
    
    # Sliding window approach
    for right in range(len(nums)):
        # Expand the window
        curr_product *= nums[right]
        
        # Shrink the window if product exceeds k
        while left <= right and curr_product >= k:
            curr_product //= nums[left]
            left += 1
        
        # Count subarrays ending at right index
        total_subarrays += right - left + 1
    
    return total_subarrays