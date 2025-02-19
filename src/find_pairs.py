def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the input list that sum up to the target.
    
    Args:
        numbers (list): List of integers to search for pairs
        target (int): Target sum to find pairs for
    
    Returns:
        list: A list of unique pairs (as tuples) that sum up to the target
    """
    # Convert to set for faster lookup
    num_set = set(numbers)
    
    # Use a set to store unique pairs to avoid duplicates
    unique_pairs = set()
    
    for num in numbers:
        complement = target - num
        
        # Check if complement exists and isn't the same index
        if complement in num_set and complement != num:
            # Create a sorted tuple to ensure unique representation
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
    
    return list(unique_pairs)