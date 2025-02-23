def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the given list that sum up to the target.

    Args:
        numbers (list): A list of numbers to search through
        target (int/float): The target sum to find pairs for

    Returns:
        list: A list of unique pairs (as tuples) that sum to the target

    Raises:
        TypeError: If input is not a list or target is not a number
        ValueError: If numbers cannot be used in arithmetic operations
    """
    # Validate input types
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a number")
    
    # Use set for unique pairs and O(n) time complexity
    seen = set()
    unique_pairs = set()

    for num in numbers:
        # Validate each number can be used arithmetically
        try:
            complement = target - num
        except TypeError:
            raise ValueError("List contains elements that cannot be used in arithmetic")
        
        # Check if the complement exists in previously seen numbers
        if complement in seen:
            # Create pair with smaller number first to ensure uniqueness
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
        
        # Add current number to seen set
        seen.add(num)
    
    return list(unique_pairs)