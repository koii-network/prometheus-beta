def bucket_sort(arr, num_buckets=10):
    """
    Implement the bucket sort algorithm.
    
    Args:
        arr (list): The input list of numbers to be sorted.
        num_buckets (int, optional): Number of buckets to use. Defaults to 10.
    
    Returns:
        list: A sorted list of numbers.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric values.
        ValueError: If the list is empty or num_buckets is less than 1.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    if num_buckets < 1:
        raise ValueError("Number of buckets must be at least 1")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Handle single element list
    if len(arr) == 1:
        return arr.copy()
    
    # Find min and max to calculate bucket range
    min_val, max_val = min(arr), max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        # Calculate bucket index
        index = int(((num - min_val) / (max_val - min_val)) * (num_buckets - 1))
        buckets[index].append(num)
    
    # Sort individual buckets
    for i in range(num_buckets):
        buckets[i].sort()
    
    # Concatenate sorted buckets
    sorted_arr = [item for bucket in buckets for item in bucket]
    
    return sorted_arr