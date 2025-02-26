def compute_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.

    Args:
        numbers (list): A list of numeric values to be weighted.
        weights (list): A list of weights corresponding to the numbers.

    Returns:
        float: The total weighted sum of the numbers.

    Raises:
        ValueError: If the lengths of numbers and weights lists are not equal,
                    or if either list is empty.
        TypeError: If the input lists contain non-numeric values.
    """
    # Validate input
    if not numbers or not weights:
        raise ValueError("Input lists cannot be empty")
    
    if len(numbers) != len(weights):
        raise ValueError("Lists of numbers and weights must have the same length")
    
    # Validate that all inputs are numeric
    try:
        numbers = [float(num) for num in numbers]
        weights = [float(weight) for weight in weights]
    except (TypeError, ValueError):
        raise TypeError("All numbers and weights must be numeric")
    
    # Compute weighted sum
    return sum(num * weight for num, weight in zip(numbers, weights))