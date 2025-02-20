def compute_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.
    
    Args:
        numbers (list): A list of numeric values to be weighted.
        weights (list): A list of weights corresponding to each number.
    
    Returns:
        float: The total weighted sum.
    
    Raises:
        ValueError: If the lengths of numbers and weights lists are different,
                    or if either list is empty.
    """
    # Validate input
    if not numbers or not weights:
        raise ValueError("Both numbers and weights lists must be non-empty")
    
    if len(numbers) != len(weights):
        raise ValueError("Numbers and weights lists must have the same length")
    
    # Compute weighted sum
    return sum(num * weight for num, weight in zip(numbers, weights))