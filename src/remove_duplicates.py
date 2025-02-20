def remove_duplicates(nums):
    """
    Remove duplicate items from a list of integers while maintaining the original order.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        list: A new list with duplicates removed, preserving the original order
    """
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result