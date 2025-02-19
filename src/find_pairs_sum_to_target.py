def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in a list that sum up to the target.
    
    Args:
        numbers (list): A list of numbers to search for pairs
        target (int): The target sum
    
    Returns:
        list: A list of unique pairs that sum up to the target
    """
    # Use a set for efficient lookup
    seen = set()
    # Use a set to store unique pairs to avoid duplicates
    unique_pairs = set()
    
    for num in numbers:
        complement = target - num
        
        # Check if the complement exists in seen
        if complement in seen:
            # Sort the pair to ensure unique representation
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
        
        # Add current number to seen set
        seen.add(num)
    
    # Convert set of tuples back to list of lists
    return [list(pair) for pair in unique_pairs]