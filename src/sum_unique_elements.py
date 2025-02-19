def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Sum of unique elements in the array
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Use a set to track unique elements efficiently
    unique_elements = set()
    seen_duplicates = set()
    
    for num in arr:
        # If number is already in duplicates, skip it
        if num in seen_duplicates:
            continue
        
        # If number is already in unique_elements, it's a duplicate
        if num in unique_elements:
            unique_elements.remove(num)
            seen_duplicates.add(num)
        else:
            unique_elements.add(num)
    
    # Return the sum of remaining unique elements
    return sum(unique_elements)