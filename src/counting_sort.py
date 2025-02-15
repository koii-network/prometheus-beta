def counting_sort(arr):
    """
    Implement Counting Sort algorithm.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are non-negative integers
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # If the list is empty, return an empty list
    if not arr:
        return []
    
    # Find the maximum element to determine the range
    max_val = max(arr)
    
    # Create a counting array to store the count of each unique element
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Modify the count array to store actual position of each element
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create the output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output