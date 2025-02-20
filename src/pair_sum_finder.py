def find_pairs_with_target_sum(arr, target_sum):
    """
    Find all pairs of numbers in the array that add up to the target sum.
    
    Args:
        arr (list): A list of unique integers
        target_sum (int): The target sum to find pairs for
    
    Returns:
        list: A list of tuples, where each tuple contains a pair of numbers 
              that sum up to the target
    
    Raises:
        ValueError: If input is not a list or contains duplicate elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    # Check for duplicates
    if len(arr) != len(set(arr)):
        raise ValueError("Input array must contain unique elements")
    
    # Use a set for O(n) time complexity
    seen = set()
    pairs = []
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            # Ensure pairs are sorted to avoid duplicates
            pair = tuple(sorted((num, complement)))
            if pair not in pairs:
                pairs.append(pair)
        seen.add(num)
    
    return pairs