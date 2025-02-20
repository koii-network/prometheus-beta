def find_max_subarray_sum_with_product(arr, target_product):
    """
    Find the maximum sum of a non-empty subarray with a specified product.
    
    Args:
        arr (list): A list of positive integers
        target_product (int): The target product constraint
    
    Returns:
        int: Maximum sum of a subarray where the product of its elements equals target_product
    
    Raises:
        ValueError: If input array is empty or contains non-positive integers
    """
    # Input validation
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if any(x <= 0 for x in arr):
        raise ValueError("Input array must contain only positive integers")
    
    n = len(arr)
    max_sum = float('-inf')
    
    # Check all possible subarrays
    for start in range(n):
        current_product = 1
        current_sum = 0
        
        for end in range(start, n):
            current_product *= arr[end]
            current_sum += arr[end]
            
            # If current product matches target, update max_sum
            if current_product == target_product:
                max_sum = max(max_sum, current_sum)
    
    # If no subarray found with the target product
    if max_sum == float('-inf'):
        return 0
    
    return max_sum