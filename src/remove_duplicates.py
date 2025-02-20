def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list without using built-in functions like set() or dict().
    
    Args:
        sorted_list (list): A sorted list of integers
    
    Returns:
        list: A new list with duplicate values removed, maintaining the original order
    """
    # Handle empty list or list with single element
    if not sorted_list:
        return []
    
    # Initialize result list with the first element
    result = [sorted_list[0]]
    
    # Iterate through the remaining list
    for num in sorted_list[1:]:
        # Only add the number if it's different from the last added number
        if num != result[-1]:
            result.append(num)
    
    return result