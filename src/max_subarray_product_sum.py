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

    # Sliding window approach
    for i in range(n):
        current_product = 1
        current_sum = 0

        for j in range(i, n):
            current_product *= arr[j]
            current_sum += arr[j]

            # If product exceeds k, break inner loop
            if current_product > k:
                break

            # Update max_sum precisely when product is less than or equal to k
            if current_product <= k:
                max_sum = max(max_sum, current_sum)

    return max_sum