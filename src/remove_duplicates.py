def remove_duplicates(input_list):
    """
    Remove duplicate values from a list while maintaining the original order.
    
    Args:
        input_list (list): A list of integers to remove duplicates from.
    
    Returns:
        list: A new list with duplicates removed, preserving the original order.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Use a set to track seen values for O(1) lookup
    seen = set()
    unique_list = []
    
    for item in input_list:
        # Only add the item if it hasn't been seen before
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    
    return unique_list