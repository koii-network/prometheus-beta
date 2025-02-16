def counting_sort(arr):
    """
    Implement the counting sort algorithm for non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Counting sort only works with non-negative integers")
    
    # If list is empty, return empty list
    if not arr:
        return []
    
    # Find the maximum number to know the range of the count array
    max_val = max(arr)
    
    # Create count array and initialize with zeros
    count = [0] * (max_val + 1)
    
    # Count occurrences of each number
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of numbers
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array from right to left
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output