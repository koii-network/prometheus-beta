def unique_coordinate_combinations(coordinates):
    """
    Generate a list of unique coordinate combinations in ascending order.

    Args:
        coordinates (list): A list of coordinate pairs, where each pair is a tuple (x, y)

    Returns:
        list: A sorted list of unique x and y values with duplicates preserved

    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
        ValueError: If coordinate pairs are not in the correct format
    """
    # Validate input
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")

    # Validate each coordinate pair
    for coord in coordinates:
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise ValueError("Each coordinate must be a tuple of (x, y)")
        if not all(isinstance(val, (int, float)) for val in coord):
            raise ValueError("Coordinates must be numeric values")

    # Extract x and y values with duplicates
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]

    # Combine values and sort 
    unique_coords = sorted(x_values + y_values)

    return unique_coords