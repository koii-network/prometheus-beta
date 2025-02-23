def counting_sort(arr):
    """
    Implement Counting Sort algorithm for sorting a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list containing the same elements as the input.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Check for non-integer or negative values
    for num in arr:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        if num < 0:
            raise ValueError("Input cannot contain negative numbers")
    
    # Find the maximum value to determine count array size
    max_val = max(arr)
    
    # Create count array initialized with zeros
    count = [0] * (max_val + 1)
    
    # Count occurrences of each unique number
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual positions of numbers
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output