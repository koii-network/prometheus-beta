def get_unique_coordinate_combinations(coordinates):
    """
    Generate a list of unique x and y values from input coordinate pairs in ascending order.

    Args:
        coordinates (list): A list of coordinate pairs, where each pair is a tuple (x, y)

    Returns:
        list: A sorted list of unique coordinate combinations

    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
        ValueError: If coordinate pairs are not in the correct format
    """
    # Input validation
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate coordinate pairs
    try:
        x_values = sorted(set(coord[0] for coord in coordinates))
        y_values = sorted(set(coord[1] for coord in coordinates))
    except (IndexError, TypeError):
        raise ValueError("Invalid coordinate pairs. Each pair must be a tuple of two numbers")
    
    # Generate unique combinations of x and y values
    unique_combinations = [(x, y) for x in x_values for y in y_values]
    
    return unique_combinations