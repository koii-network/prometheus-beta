def get_unique_pairs(numbers):
    """
    Returns all unique pairs of elements from a given list of integers.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list of tuples, where each tuple is a unique pair of elements
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check that all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers")
    
    # Use a set to track unique pairs (sorted to avoid duplicates)
    unique_pairs = set()
    
    # Remove duplicates while preserving order
    unique_nums = list(dict.fromkeys(numbers))
    
    # Generate all unique pairs
    for i in range(len(unique_nums)):
        for j in range(i+1, len(unique_nums)):
            # Sort the pair to ensure (a,b) and (b,a) are considered the same
            pair = tuple(sorted((unique_nums[i], unique_nums[j])))
            unique_pairs.add(pair)
    
    return list(unique_pairs)