def compute_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.

    Args:
        numbers (list): A list of numeric values to be summed.
        weights (list): A list of weights corresponding to the numbers.

    Returns:
        float: The total weighted sum of the numbers.

    Raises:
        ValueError: If the lengths of numbers and weights lists do not match,
                    if either list is empty, or if lists contain non-numeric values.
    """
    # Validate input
    if not numbers or not weights:
        raise ValueError("Input lists cannot be empty")
    
    if len(numbers) != len(weights):
        raise ValueError("Numbers and weights lists must have the same length")
    
    # Convert to floats and validate numeric inputs
    try:
        float_numbers = []
        float_weights = []
        for num, weight in zip(numbers, weights):
            # Attempt conversion to float
            converted_num = float(num)
            converted_weight = float(weight)
            float_numbers.append(converted_num)
            float_weights.append(converted_weight)
    except (TypeError, ValueError):
        raise ValueError("All numbers and weights must be numeric")
    
    # Compute weighted sum
    return sum(num * weight for num, weight in zip(float_numbers, float_weights))