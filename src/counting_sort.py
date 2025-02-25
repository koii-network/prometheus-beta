def counting_sort(arr):
    """
    Implement the counting sort algorithm for sorting a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains negative numbers.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Check for negative numbers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("List must contain only non-negative integers")
    
    # Find the maximum element to determine range
    max_val = max(arr)
    
    # Create counting array and initialize with zeros
    count = [0] * (max_val + 1)
    
    # Count occurrences of each unique number
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of each number
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output