def remove_duplicates(integers):
    """
    Remove duplicate items from a list of integers while maintaining original order.
    
    Args:
        integers (list): A list of integers
    
    Returns:
        list: A new list with duplicates removed, preserving the original order
    """
    seen = set()
    result = []
    for num in integers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result