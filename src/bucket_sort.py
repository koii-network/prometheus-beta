def bucket_sort(arr, bucket_count=10):
    """
    Implements the bucket sort algorithm.
    
    Args:
        arr (list): The input list of numbers to be sorted.
        bucket_count (int, optional): Number of buckets to use. Defaults to 10.
    
    Returns:
        list: A sorted version of the input list.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If input list is empty.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Find min and max to determine bucket ranges
    if len(arr) == 1:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    
    # Prevent division by zero
    if min_val == max_val:
        return arr
    
    # Create buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribute elements into buckets
    for num in arr:
        # Calculate bucket index
        bucket_index = int(((num - min_val) / (max_val - min_val)) * (bucket_count - 1))
        buckets[bucket_index].append(num)
    
    # Sort individual buckets
    sorted_buckets = [sorted(bucket) for bucket in buckets]
    
    # Flatten sorted buckets
    return [num for bucket in sorted_buckets for num in bucket]