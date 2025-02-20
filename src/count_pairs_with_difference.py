def count_pairs_with_difference_of_five(numbers):
    """
    Count the number of adjacent pairs in the list with a difference of 5.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Number of adjacent pairs with a difference of 5
    
    Examples:
        >>> count_pairs_with_difference_of_five([1, 6, 3, 8, 9, 4])
        2
        >>> count_pairs_with_difference_of_five([1, 2, 3, 4, 5])
        0
    """
    if not numbers or len(numbers) < 2:
        return 0
    
    pair_count = 0
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) == 5:
            pair_count += 1
    
    return pair_count