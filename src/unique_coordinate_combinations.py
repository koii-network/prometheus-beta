def get_unique_coordinate_combinations(coordinates):
    """
    Takes a list of coordinate pairs and returns a list of unique combinations 
    of x and y values in ascending order.
    
    Args:
        coordinates (list): List of coordinate tuples [(x1, y1), (x2, y2), ...]
    
    Returns:
        list: Sorted list of unique x and y values
    
    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
        ValueError: If coordinate pairs are not in correct format
    """
    # Input validation
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate coordinate pairs
    try:
        x_values = set()
        y_values = set()
        
        for coord in coordinates:
            if not isinstance(coord, (list, tuple)) or len(coord) != 2:
                raise ValueError(f"Invalid coordinate pair: {coord}")
            
            x, y = coord
            if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
                raise ValueError(f"Coordinates must be numeric: {coord}")
            
            x_values.add(x)
            y_values.add(y)
        
        # Combine and sort unique values
        unique_combinations = sorted(list(x_values.union(y_values)))
        
        return unique_combinations
    
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")