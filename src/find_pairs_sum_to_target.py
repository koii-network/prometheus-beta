def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the list that sum up to the target.
    
    Args:
        numbers (list): List of numbers to search through
        target (int): Target sum to find pairs for
    
    Returns:
        list: A list of unique pairs that sum to the target
    """
    # Use a set for efficient lookups
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        
        # Check if the complement exists and is not the same as the current number
        if complement in seen and complement != num:
            # Sort the pair to ensure uniqueness
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        
        seen.add(num)
    
    # Convert set of tuples back to list of lists
    return [list(pair) for pair in pairs]