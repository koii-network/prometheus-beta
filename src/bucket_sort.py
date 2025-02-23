def bucket_sort(arr, bucket_count=10):
    """
    Implement the bucket sort algorithm for sorting a list of numbers.
    
    Args:
        arr (list): The input list of numbers to be sorted.
        bucket_count (int, optional): Number of buckets to use. Defaults to 10.
    
    Returns:
        list: A sorted list of numbers.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If bucket count is less than 1.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if len(arr) == 0:
        return []
    
    # Validate bucket count
    if bucket_count < 1:
        raise ValueError("Bucket count must be at least 1")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Find min and max to determine range
    if len(arr) == 0:
        return []
    
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Create buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribute elements into buckets
    value_range = max_val - min_val
    for num in arr:
        # Calculate bucket index
        bucket_index = min(
            bucket_count - 1, 
            int(((num - min_val) / value_range) * (bucket_count - 1))
        )
        buckets[bucket_index].append(num)
    
    # Sort individual buckets
    sorted_buckets = []
    for bucket in buckets:
        # Use Python's built-in sort for individual buckets
        bucket.sort()
        sorted_buckets.extend(bucket)
    
    return sorted_buckets