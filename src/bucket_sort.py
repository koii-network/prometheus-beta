def bucket_sort(arr, num_buckets=10):
    """
    Implement the bucket sort algorithm for sorting a list of numbers.
    
    Args:
        arr (list): The input list of numbers to be sorted.
        num_buckets (int, optional): Number of buckets to use. Defaults to 10.
    
    Returns:
        list: A sorted version of the input list.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Handle single element list
    if len(arr) == 1:
        return arr.copy()
    
    # Find min and max to determine bucket range
    min_val, max_val = min(arr), max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Create buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        # Calculate bucket index
        bucket_index = int(((num - min_val) / (max_val - min_val)) * (num_buckets - 1))
        buckets[bucket_index].append(num)
    
    # Sort individual buckets
    sorted_buckets = []
    for bucket in buckets:
        # Use Python's built-in sort for individual buckets
        bucket.sort()
        sorted_buckets.extend(bucket)
    
    return sorted_buckets