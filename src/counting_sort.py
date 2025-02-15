def counting_sort(arr):
    """
    Implement Counting Sort algorithm for non-negative integers.
    
    Args:
        arr (list): List of non-negative integers to be sorted
    
    Returns:
        list: Sorted list of integers
    
    Raises:
        ValueError: If input contains negative numbers
        TypeError: If input is not a list or contains non-integer elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check for non-integer or negative numbers
    if any(not isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Counting sort only works with non-negative integers")
    
    # Find the range of the input
    max_val = max(arr)
    
    # Create counting array and initialize with zeros
    count = [0] * (max_val + 1)
    
    # Count occurrences of each unique integer
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of each object
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output