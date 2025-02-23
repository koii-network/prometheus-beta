def find_second_highest(sorted_list):
    """
    Find the second highest value in a sorted list of integers.
    
    Args:
        sorted_list (list): A sorted list of integers in ascending or descending order.
    
    Returns:
        int or None: The second highest value in the list, or None if the list 
                     has fewer than 2 unique elements.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Validate input type
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Validate list elements
    if not all(isinstance(x, int) for x in sorted_list):
        raise ValueError("List must contain only integers")
    
    # Handle empty or single-element lists
    if len(sorted_list) < 2:
        return None
    
    # Remove duplicates while preserving order
    unique_list = []
    for num in sorted_list:
        if num not in unique_list:
            unique_list.append(num)
    
    # Return None if fewer than 2 unique elements
    if len(unique_list) < 2:
        return None
    
    # Return the second highest value (second to last element)
    return unique_list[-2]