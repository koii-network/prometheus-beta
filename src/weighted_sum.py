def compute_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.
    
    Args:
        numbers (list): A list of numbers to be weighted
        weights (list): A list of weights corresponding to the numbers
    
    Returns:
        float: The total weighted sum
    
    Raises:
        ValueError: If the lengths of numbers and weights are not equal
    """
    if len(numbers) != len(weights):
        raise ValueError("The number of elements in 'numbers' and 'weights' must be the same")
    
    return sum(num * weight for num, weight in zip(numbers, weights))