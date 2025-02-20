def remove_duplicates(input_list):
    """
    Remove duplicate items from a list of integers while maintaining the original order.
    
    Args:
        input_list (list): A list of integers
    
    Returns:
        list: A new list with duplicates removed, preserving the original order
    """
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result