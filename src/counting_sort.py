def counting_sort(arr):
    """
    Implement the counting sort algorithm for sorting a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Check for negative numbers
    if any(x < 0 for x in arr):
        raise ValueError("Counting sort only works with non-negative integers")
    
    # Handle empty list
    if not arr:
        return []
    
    # Find the maximum number to know the range of counts
    max_num = max(arr)
    
    # Create a count array to store count of each unique object
    count = [0] * (max_num + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of each object
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create the output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output