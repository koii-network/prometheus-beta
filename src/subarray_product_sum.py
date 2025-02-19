def count_subarrays_with_product_less_than_k(nums, k):
    """
    Count the number of subarrays with product less than k.
    
    :param nums: List of integers
    :param k: Integer threshold for product
    :return: Sum of all subarrays with product less than k
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # If k is less than or equal to 1, no subarrays possible
    if k <= 1:
        return 0
    
    total_sum = 0
    n = len(nums)
    
    # Iterate through all possible starting points
    for start in range(n):
        # Track the current product for the running subarray
        current_product = 1
        
        # Extend the subarray and track valid subarrays
        for end in range(start, n):
            # Multiply current element to the product
            current_product *= nums[end]
            
            # If product exceeds k, stop this inner iteration
            if current_product >= k:
                break
            
            # Sum the current subarray values
            total_sum += sum(nums[start:end+1])
    
    return total_sum