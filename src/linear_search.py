def linear_search(nums: list[int], target: int) -> int:
    """
    Perform a linear search to find the index of the target value in the list.
    
    Args:
        nums (list[int]): The list of integers to search through
        target (int): The value to find in the list
    
    Returns:
        int: The index of the first occurrence of the target, or -1 if not found
    """
    for index, value in enumerate(nums):
        if value == target:
            return index
    return -1