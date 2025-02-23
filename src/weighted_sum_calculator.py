def calculate_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.
    
    Args:
        numbers (list): A list of numbers to be weighted
        weights (list): A list of weights corresponding to the numbers
    
    Returns:
        float: The total weighted sum
    
    Raises:
        ValueError: If the lengths of numbers and weights are not equal
        TypeError: If inputs are not lists or contain non-numeric values
    """
    # Validate inputs
    if not isinstance(numbers, list) or not isinstance(weights, list):
        raise TypeError("Inputs must be lists")
    
    if len(numbers) != len(weights):
        raise ValueError("Number of numbers and weights must be equal")
    
    # Validate numeric values
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Numbers must be numeric")
    
    if not all(isinstance(weight, (int, float)) for weight in weights):
        raise TypeError("Weights must be numeric")
    
    # Calculate weighted sum
    try:
        weighted_sum = sum(num * weight for num, weight in zip(numbers, weights))
        return weighted_sum
    except Exception as e:
        raise ValueError(f"Error computing weighted sum: {str(e)}")