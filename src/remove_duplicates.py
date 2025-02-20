def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list without using built-in functions like set() or dict().
    
    Args:
        sorted_list (list): A sorted list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the original order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list is not sorted
    """
    # Check input type
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if not sorted_list:
        return []
    
    # Validate that the list is sorted
    if sorted_list != sorted(sorted_list):
        raise ValueError("Input list must be sorted")
    
    # Remove duplicates by comparing adjacent elements
    result = [sorted_list[0]]
    for num in sorted_list[1:]:
        if num != result[-1]:
            result.append(num)
    
    return result