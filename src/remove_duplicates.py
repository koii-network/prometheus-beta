def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list without using built-in set() or dict().
    
    Args:
        sorted_list (list): A sorted list of integers
    
    Returns:
        list: A new list with duplicate values removed, maintaining the original order
    """
    # If the list is empty or has only one element, return it as-is
    if len(sorted_list) <= 1:
        return sorted_list.copy()
    
    # Initialize result list with the first element
    result = [sorted_list[0]]
    
    # Iterate through the rest of the list
    for num in sorted_list[1:]:
        # Only add the number if it's different from the last added number
        if num != result[-1]:
            result.append(num)
    
    return result