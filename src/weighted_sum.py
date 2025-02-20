def compute_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.
    
    Args:
        numbers (list): A list of numeric values to be weighted
        weights (list): A list of weights corresponding to each number
    
    Returns:
        float: The total weighted sum
    
    Raises:
        ValueError: If the lengths of numbers and weights are not equal
        TypeError: If inputs are not lists or contain non-numeric values
    """
    # Input validation
    if not isinstance(numbers, list) or not isinstance(weights, list):
        raise TypeError("Both numbers and weights must be lists")
    
    if len(numbers) != len(weights):
        raise ValueError("Numbers and weights lists must have the same length")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in numbers + weights):
        raise TypeError("All elements must be numeric")
    
    # Compute weighted sum
    weighted_sum = sum(num * weight for num, weight in zip(numbers, weights))
    
    return weighted_sum