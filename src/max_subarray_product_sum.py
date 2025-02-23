def find_max_subarray_product_sum(arr, target_product):
    """
    Find the maximum sum of a non-empty subarray with a specified product.
    
    Args:
        arr (list): A list of positive integers
        target_product (int): The target product to match
    
    Returns:
        int: Maximum sum of a subarray that has a product equal to target_product
        None: If no such subarray exists
    
    Raises:
        ValueError: If input array is empty or contains non-positive integers
    """
    # Validate input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if any(x <= 0 for x in arr):
        raise ValueError("Input array must contain only positive integers")
    
    n = len(arr)
    max_sum = None
    
    # Try all possible subarrays
    for start in range(n):
        current_product = 1
        current_sum = 0
        
        for end in range(start, n):
            current_product *= arr[end]
            current_sum += arr[end]
            
            # Check if current subarray meets the product requirement
            if current_product == target_product:
                # Update max_sum if this is the first match or sum is larger
                if max_sum is None or current_sum > max_sum:
                    max_sum = current_sum
    
    return max_sum