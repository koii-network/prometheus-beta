def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Time complexity: O(n)
    Space complexity: O(n)
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Sum of unique elements in the array
    
    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Use a set to track unique elements efficiently
    unique_elements = set()
    unique_sum = 0
    
    # Single pass through the array
    for num in arr:
        # Ensure input contains only integers
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        # If this is the first occurrence of the number, add to sum
        if num not in unique_elements:
            unique_elements.add(num)
            unique_sum += num
    
    return unique_sum