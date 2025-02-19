def find_index(numbers, target):
    """
    Find the index of the first occurrence of a target value in a list of integers.
    
    Args:
        numbers (list): A list of integers to search through
        target (int): The value to find in the list
    
    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found
    """
    for index, num in enumerate(numbers):
        if num == target:
            return index
    return -1