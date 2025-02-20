def find_two_sum_pairs(arr, target_sum):
    """
    Find all unique pairs of numbers in the array that add up to the target sum.
    
    Args:
        arr (list): A list of unique integers
        target_sum (int): The target sum to find pairs for
    
    Returns:
        list: A list of tuples, where each tuple contains a pair of numbers that sum to target_sum
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target_sum, (int, float)):
        raise TypeError("Target sum must be a number")
    
    # Use a set for O(n) time complexity
    seen = set()
    pairs = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            # Ensure pairs are sorted to avoid duplicates
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)
    
    return list(pairs)