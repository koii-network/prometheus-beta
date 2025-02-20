def count_difference_five_pairs(numbers):
    """
    Count the number of pairs of integers in the list with a difference of 5.
    A pair is defined as two distinct integers that appear next to each other in the list.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Number of pairs with a difference of 5
    
    Examples:
        >>> count_difference_five_pairs([1, 6, 3, 8, 2, 7])
        2
        >>> count_difference_five_pairs([1, 2, 3, 4, 5])
        0
    """
    if not numbers or len(numbers) < 2:
        return 0
    
    pair_count = 0
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) == 5:
            pair_count += 1
    
    return pair_count