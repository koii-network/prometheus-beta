def get_unique_coordinate_combinations(coordinates):
    """
    Takes a list of coordinate pairs and returns a list of unique combinations 
    of x and y values in ascending order.
    
    Args:
        coordinates (list): A list of coordinate tuples (x, y)
    
    Returns:
        list: A sorted list of unique coordinate combinations
    
    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
    """
    # Validate input 
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate each coordinate pair
    for coord in coordinates:
        if not (isinstance(coord, (list, tuple)) and len(coord) == 2):
            raise TypeError("Each coordinate must be a pair of values")
    
    # Extract unique x and y values, then sort
    unique_x = sorted(set(coord[0] for coord in coordinates))
    unique_y = sorted(set(coord[1] for coord in coordinates))
    
    # Generate all unique combinations 
    unique_combinations = []
    for x in unique_x:
        for y in unique_y:
            unique_combinations.append((x, y))
    
    return sorted(unique_combinations)