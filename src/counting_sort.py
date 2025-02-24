def counting_sort(arr):
    """
    Implement Counting Sort algorithm for a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains negative numbers.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Find the range of the input
    try:
        max_val = max(arr)
        min_val = min(arr)
    except TypeError:
        raise TypeError("List must contain comparable elements")
    
    # Check for negative numbers
    if min_val < 0:
        raise ValueError("Counting sort only works with non-negative integers")
    
    # Create counting array
    count = [0] * (max_val + 1)
    
    # Count occurrences of each unique object
    for num in arr:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        count[num] += 1
    
    # Modify count array to store actual position of each object
    output = []
    for i in range(len(count)):
        # Append the number 'count[i]' times
        output.extend([i] * count[i])
    
    return output