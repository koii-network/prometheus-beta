def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list of integers.
    
    Args:
        sorted_list (list): A sorted list of integers.
    
    Returns:
        list: A new list with duplicate values removed while maintaining order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is not sorted.
    """
    # Check if input is a list
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not sorted_list:
        return []
    
    # Check if list is sorted
    if any(sorted_list[i] > sorted_list[i+1] for i in range(len(sorted_list)-1)):
        raise ValueError("Input list must be sorted")
    
    # Remove duplicates while preserving order
    unique_list = []
    for num in sorted_list:
        # Only add the number if it's not already in the unique list
        if not unique_list or num > unique_list[-1]:
            unique_list.append(num)
    
    return unique_list