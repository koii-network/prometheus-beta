def counting_sort(arr):
    """
    Implement the counting sort algorithm for non-negative integers.
    
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
    
    # Handle empty list case
    if not arr:
        return []
    
    # Check for non-integer or negative elements
    for num in arr:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        if num < 0:
            raise ValueError("Counting sort only works with non-negative integers")
    
    # Find the maximum number to know the range of count array
    max_num = max(arr)
    
    # Create count array and initialize with zeros
    count = [0] * (max_num + 1)
    
    # Count occurrences of each number
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of numbers
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output