def get_unique_coordinate_combinations(coordinates):
    """
    Generate a list of unique x and y values from given coordinate pairs in ascending order.
    
    Args:
        coordinates (list): A list of coordinate pairs, where each pair is a tuple (x, y)
    
    Returns:
        list: A list of tuples with unique (x, y) combinations in ascending order
    
    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
    """
    # Validate input
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate each coordinate pair
    for coord in coordinates:
        if not (isinstance(coord, (list, tuple)) and len(coord) == 2):
            raise TypeError("Each coordinate must be a pair (x, y)")
    
    # Extract unique x and y values, sort them
    unique_x = sorted(set(coord[0] for coord in coordinates))
    unique_y = sorted(set(coord[1] for coord in coordinates))
    
    # Generate unique combinations
    unique_combinations = [(x, y) for x in unique_x for y in unique_y]
    
    return unique_combinations