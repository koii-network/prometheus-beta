def get_unique_coordinate_combinations(coordinates):
    """
    Find unique x and y values from a list of coordinate pairs in ascending order.

    Args:
        coordinates (list): A list of coordinate pairs, where each pair is a tuple (x, y)

    Returns:
        list: A sorted list of unique x and y values

    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
        ValueError: If coordinate pairs are not in correct format
    """
    # Validate input is a list
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate each coordinate pair
    unique_values = set()
    for coord in coordinates:
        # Check each coordinate pair is a tuple or list with 2 elements
        if not (isinstance(coord, (tuple, list)) and len(coord) == 2):
            raise ValueError(f"Invalid coordinate pair: {coord}. Must be a tuple or list with 2 elements.")
        
        # Ensure coordinate values are numbers
        try:
            x, y = float(coord[0]), float(coord[1])
        except (TypeError, ValueError):
            raise ValueError(f"Coordinate values must be numeric: {coord}")
        
        # Add x and y to unique values
        unique_values.add(x)
        unique_values.add(y)
    
    # Return sorted unique values
    return sorted(unique_values)