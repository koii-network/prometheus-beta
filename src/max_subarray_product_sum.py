def find_max_subarray_product_sum(arr, k):
    """
    Find the maximum sum of a non-empty subarray with a specified product.

    Args:
        arr (list[int]): Input array of positive integers
        k (int): Target product constraint

    Returns:
        int: Maximum sum of a subarray whose product is less than or equal to k

    Raises:
        ValueError: If input array is empty or contains non-positive integers
    """
    # Input validation
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if any(x <= 0 for x in arr):
        raise ValueError("Input array must contain only positive integers")

    n = len(arr)
    max_sum = 0

    # Use sliding window with stricter conditions
    for i in range(n):
        for j in range(i, n):
            # Calculate subarray product and sum
            current_product = 1
            current_sum = 0
            for x in range(i, j+1):
                current_product *= arr[x]
                current_sum += arr[x]

            # Check product constraint specifically
            if current_product <= k:
                max_sum = max(max_sum, current_sum)

    return max_sum