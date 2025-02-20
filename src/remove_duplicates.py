def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list of integers without using built-in functions.
    
    Args:
        sorted_list (list): A sorted list of integers
    
    Returns:
        list: A new list with duplicate values removed
    """
    # If the list is empty or None, return an empty list
    if not sorted_list:
        return []
    
    # Initialize result list with the first element
    result = [sorted_list[0]]
    
    # Iterate through the sorted list starting from the second element
    for num in sorted_list[1:]:
        # Only add the number if it's different from the last added number
        if num != result[-1]:
            result.append(num)
    
    return result