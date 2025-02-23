def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray in the given array.
    
    A non-overlapping subarray is a contiguous part of the array that does not 
    share any indices with another selected subarray.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of non-overlapping subarrays.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Examples:
        >>> max_non_overlapping_subarray_sum([1, 2, 3, 4, 5])
        7
        >>> max_non_overlapping_subarray_sum([-1, 2, -3, 4, 5])
        7
        >>> max_non_overlapping_subarray_sum([])
        0
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return 0
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # If array has less than 2 elements, return 0 or the first positive element
    if len(arr) < 2:
        return 0
    
    # Dynamic programming to find max sum of non-overlapping subarrays
    n = len(arr)
    
    # dp[i] will store the maximum sum up to index i
    dp = [0] * n
    
    # Initialize first two elements
    dp[0] = max(arr[0], 0)
    dp[1] = max(dp[0], arr[1], 0)
    
    # Fill the dp array
    for i in range(2, n):
        # Two choices:
        # 1. Include current element with a non-overlapping previous subarray
        # 2. Exclude current element and take previous max
        dp[i] = max(
            (dp[i-2] if dp[i-2] > 0 else 0) + max(arr[i], 0),  # option 1
            dp[i-1]  # option 2
        )
    
    return max(dp[-1], dp[-2], 0)