def counting_sort(arr):
    """
    Implement the counting sort algorithm for non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element is not a non-negative integer.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are non-negative integers
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # If list is empty, return empty list
    if not arr:
        return []
    
    # Find the maximum element to determine the range
    max_val = max(arr)
    
    # Create counting array (size of max_val + 1)
    count = [0] * (max_val + 1)
    
    # Count occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual positions
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output