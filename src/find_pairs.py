def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the list that sum up to the target.
    
    Args:
        numbers (list): A list of numbers to search through
        target (int): The target sum to find pairs for
    
    Returns:
        list: A list of unique pairs (as tuples) that sum to the target
    """
    # Use a set for efficient lookup
    seen = set()
    # Use a set to store unique pairs to avoid duplicates
    unique_pairs = set()
    
    for num in numbers:
        complement = target - num
        
        # Check if the complement exists in seen numbers
        if complement in seen:
            # Create a pair with the smaller number first to avoid duplicates
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
        
        # Add current number to seen set
        seen.add(num)
    
    return list(unique_pairs)