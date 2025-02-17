def counting_sort(arr):
    """
    Implement Counting Sort algorithm.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Find the maximum element to determine the range
    max_val = max(arr)
    
    # Create counting array to store count of each unique element
    count = [0] * (max_val + 1)
    
    # Count occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of elements
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output