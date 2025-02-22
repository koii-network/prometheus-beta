def get_unique_coordinate_combinations(coordinates):
    """
    Takes a list of coordinate pairs and returns a list of unique x and y values in ascending order.
    
    Args:
        coordinates (list): A list of tuples representing (x, y) coordinates
    
    Returns:
        list: A list of unique coordinate combinations sorted in ascending order
    
    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
    """
    # Input validation
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate each coordinate pair
    for coord in coordinates:
        if not (isinstance(coord, tuple) and len(coord) == 2 and 
                all(isinstance(val, (int, float)) for val in coord)):
            raise TypeError("Each coordinate must be a tuple of two numeric values")
    
    # Extract unique x and y values, sort them
    unique_x = sorted(set(coord[0] for coord in coordinates))
    unique_y = sorted(set(coord[1] for coord in coordinates))
    
    # Create combinations
    unique_combinations = [(x, y) for x in unique_x for y in unique_y]
    
    return unique_combinations