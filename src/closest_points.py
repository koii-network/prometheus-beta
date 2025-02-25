import math
from typing import List, Tuple, Optional

def find_closest_points(list_a: List[Tuple[float, float]], 
                        list_b: List[Tuple[float, float]]) -> Optional[Tuple[Tuple[float, float], Tuple[float, float]]]:
    """
    Find the two closest points, one from list A and one from list B, 
    using Euclidean distance.
    
    Args:
        list_a (List[Tuple[float, float]]): First list of points (x, y coordinates)
        list_b (List[Tuple[float, float]]): Second list of points (x, y coordinates)
    
    Returns:
        Optional[Tuple[Tuple[float, float], Tuple[float, float]]]: 
        A tuple of two points (one from A, one from B) with the smallest distance,
        or None if either input list is empty
    
    Raises:
        TypeError: If inputs are not lists of tuples
        ValueError: If points do not have exactly 2 coordinates
    
    Time Complexity: O(n*m), where n and m are lengths of list_a and list_b
    Space Complexity: O(1)
    """
    # Input validation
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Inputs must be lists")
    
    # Check for empty lists
    if not list_a or not list_b:
        return None
    
    # Validate point formats
    for point in list_a + list_b:
        if not isinstance(point, tuple) or len(point) != 2:
            raise ValueError("Points must be 2D tuples")
        if not all(isinstance(coord, (int, float)) for coord in point):
            raise TypeError("Point coordinates must be numeric")
    
    # Initialize variables
    min_distance = float('inf')
    closest_points = None
    
    # Nested loops to compare all points
    for point_a in list_a:
        for point_b in list_b:
            # Calculate Euclidean distance
            distance = math.sqrt(
                (point_a[0] - point_b[0])**2 + 
                (point_a[1] - point_b[1])**2
            )
            
            # Update if new minimum distance found
            if distance < min_distance:
                min_distance = distance
                closest_points = (point_a, point_b)
    
    return closest_points