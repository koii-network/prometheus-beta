def remove_unique_elements(my_list):
    """
    Remove unique elements from a list of integers, keeping only elements 
    that appear more than once, in their original order.
    
    Uses only built-in list methods to identify and remove unique elements.
    
    Args:
        my_list (list): A list of integers to process
    
    Returns:
        list: A new list containing only elements that appear multiple times
    
    Examples:
        >>> remove_unique_elements([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 2, 1]
        >>> remove_unique_elements([1, 2, 3, 4, 5])
        []
        >>> remove_unique_elements([])
        []
    """
    # Handle empty list edge case
    if not my_list:
        return []
    
    # Create a result list to store duplicates
    duplicates = []
    
    # Iterate through the list in original order
    for item in my_list:
        # If this is the first occurrence and it appears again later, add it
        if my_list.count(item) > 1 and item not in duplicates:
            # Add the required number of occurrences of this duplicate
            multiple_count = my_list.count(item)
            duplicates.extend([item] * multiple_count)
            
            # Prevent re-adding the same duplicate type
            duplicates.remove(item)
    
    return duplicates