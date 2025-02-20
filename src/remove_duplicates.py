def remove_duplicates(input_list):
    """
    Remove duplicate items from a list of integers while maintaining the original order.
    
    Args:
        input_list (list): A list of integers with potential duplicates
    
    Returns:
        list: A new list with duplicates removed, preserving the order of first appearance
    """
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result