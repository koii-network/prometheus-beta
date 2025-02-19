def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the list that sum up to the target.
    
    Args:
        numbers (list): A list of numbers to search through
        target (int): The target sum to find pairs for
    
    Returns:
        list: A list of unique pairs (as tuples) that sum to the target
    """
    # Use a set for O(n) time complexity and to avoid duplicate pairs
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        
        # Check if the complement exists in seen numbers
        if complement in seen:
            # Always store pairs in sorted order to avoid duplicates
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        
        # Add current number to seen set
        seen.add(num)
    
    return list(pairs)