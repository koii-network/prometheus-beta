def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Sum of unique elements in the array
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a list
        TypeError: If list contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Use a dictionary to track element frequency
    element_count = {}
    unique_sum = 0
    
    # First pass: Count frequencies
    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1
    
    # Second pass: Sum unique elements
    for num, count in element_count.items():
        if count == 1:
            unique_sum += num
    
    return unique_sum