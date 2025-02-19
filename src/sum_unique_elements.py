def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Sum of unique elements
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not arr:
        return 0
    
    # Use a set to track unique elements efficiently
    unique_elements = set()
    duplicates = set()
    
    for num in arr:
        # If number is already in unique_elements, it's a duplicate
        if num in unique_elements:
            duplicates.add(num)
        else:
            unique_elements.add(num)
    
    # Sum of unique elements is the sum of unique_elements minus the duplicates
    return sum(unique_elements - duplicates)