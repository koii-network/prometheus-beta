def find_smallest_sum(list1, list2):
    """
    Find the smallest possible sum between two lists of integers.
    
    Args:
        list1 (list): First list of integers
        list2 (list): Second list of integers
    
    Returns:
        int: The smallest possible sum that can be created by 
             taking one element from each list
    
    Raises:
        ValueError: If either input list is empty
    """
    # Check if either list is empty
    if not list1 or not list2:
        raise ValueError("Both input lists must contain at least one element")
    
    # Initialize with the sum of the first elements of both lists
    smallest_sum = float('inf')
    
    # Compare all possible combinations
    for num1 in list1:
        for num2 in list2:
            current_sum = num1 + num2
            smallest_sum = min(smallest_sum, current_sum)
    
    return smallest_sum