def find_max_subarray_product_sum(arr, target_product):
    """
    Find the maximum sum of a non-empty subarray with a specified product.

    Args:
        arr (list): A list of positive integers.
        target_product (int): The target product to match.

    Returns:
        int: The maximum sum of a subarray with the target product.
             Returns -1 if no such subarray exists.

    Raises:
        ValueError: If input array is empty or contains non-positive integers.
    """
    # Input validation
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if any(x <= 0 for x in arr):
        raise ValueError("All integers must be positive")
    
    n = len(arr)
    max_sum = -1

    # Check all possible subarrays
    for start in range(n):
        current_product = 1
        current_sum = 0

        for end in range(start, n):
            # Update current product and sum
            current_product *= arr[end]
            current_sum += arr[end]

            # Check if current subarray meets the product condition
            if current_product == target_product:
                max_sum = max(max_sum, current_sum)

    return max_sum