def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the input list that sum up to the target.

    Args:
        numbers (list): A list of integers to search for pairs.
        target (int): The target sum to find pairs for.

    Returns:
        list: A list of unique pairs (as tuples) that sum up to the target.
              Pairs are sorted in ascending order, and the list of pairs is 
              sorted to ensure uniqueness.

    Examples:
        >>> find_pairs_sum_to_target([1, 2, 3, 4, 5], 7)
        [(2, 5), (3, 4)]
        >>> find_pairs_sum_to_target([1, 1, 2, 3, 4], 5)
        [(1, 4)]
    """
    # Handle edge cases
    if not numbers or len(numbers) < 2:
        return []

    # Use a set for O(1) lookup to improve efficiency
    num_set = set()
    unique_pairs = set()

    # Iterate through the list
    for num in numbers:
        complement = target - num
        
        # Check if the complement exists in the set
        if complement in num_set:
            # Always create a sorted pair to avoid duplicates
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
        
        # Add current number to the set
        num_set.add(num)

    # Convert set to sorted list for consistent output
    return sorted(list(unique_pairs))