def gravity_sort(arr):
    """
    Implement the gravity sort (bucket sort) algorithm.
    
    Gravity sort simulates gravity by creating columns of numbers 
    and letting them 'fall' to create a sorted array.
    
    Args:
        arr (list): Input list of non-negative integers to be sorted
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains negative numbers
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Gravity sort only works with non-negative integers")
    
    # Find the maximum number to determine the number of columns
    max_num = max(arr)
    
    # Create buckets (columns) representing each number's bits
    buckets = []
    for i in range(max_num.bit_length()):
        # Create a column for each bit position
        column = [1 if (num & (1 << i)) else 0 for num in arr]
        buckets.append(column)
    
    # Let the 'buckets' fall (simulate gravity)
    sorted_arr = []
    for i in range(len(arr)):
        # Count the 1s in each column and create the number
        current_num = sum(bucket[i] << j for j, bucket in enumerate(buckets))
        sorted_arr.append(current_num)
    
    return sorted(sorted_arr)