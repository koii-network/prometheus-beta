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
    
    # Use a set to track unique elements
    unique_elements = set()
    
    # Sum of unique elements
    unique_sum = 0
    
    # Iterate through the array once - O(n) time complexity
    for num in arr:
        # If this is the first occurrence of the number
        if num not in unique_elements:
            unique_elements.add(num)
            unique_sum += num
        # If number is already in unique_elements, it's a duplicate, 
        # so we remove it to ensure it's not counted again
        else:
            unique_elements.discard(num)
            unique_sum -= num
    
    return unique_sum