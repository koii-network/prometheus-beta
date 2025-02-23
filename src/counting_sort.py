def counting_sort(arr):
    """
    Implement Counting Sort algorithm for sorting a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements.
        ValueError: If input contains negative numbers.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Check for non-integer elements and negative numbers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Input must contain only non-negative integers")
    
    # Find the maximum number to know the range of the array
    max_val = max(arr)
    
    # Create a count array to store count of each unique number
    count = [0] * (max_val + 1)
    
    # Store the count of each number
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