def find_two_sum(numbers, target_sum):
    """
    Find all unique pairs of numbers in the array that add up to the target sum.
    
    Args:
        numbers (list): A list of unique integers
        target_sum (int): The target sum to find pairs for
    
    Returns:
        list: A list of tuples, where each tuple contains a pair of numbers 
              that add up to the target sum
    """
    # Use a set for O(1) lookup to improve efficiency
    num_set = set(numbers)
    pairs = []
    
    # Iterate through the numbers to find pairs
    for num in numbers:
        complement = target_sum - num
        
        # Check if complement exists in the set and is not the same number
        if complement in num_set and complement != num:
            # Sort the pair to avoid duplicates and ensure consistent order
            pair = tuple(sorted((num, complement)))
            
            # Add the pair only if it's not already in the list
            if pair not in pairs:
                pairs.append(pair)
    
    return pairs