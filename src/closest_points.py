import math
from typing import List, Tuple, Optional

def find_closest_points(points_a: List[Tuple[float, float]], 
                        points_b: List[Tuple[float, float]]) -> Optional[Tuple[Tuple[float, float], Tuple[float, float]]]:
    """
    Find the two closest points, one from list A and one from list B, 
    using Euclidean distance.
    
    Args:
        points_a (List[Tuple[float, float]]): First list of points (x, y coordinates)
        points_b (List[Tuple[float, float]]): Second list of points (x, y coordinates)
    
    Returns:
        Optional[Tuple[Tuple[float, float], Tuple[float, float]]]: 
        Tuple of the two closest points (one from A, one from B), 
        or None if either input list is empty
    
    Raises:
        TypeError: If inputs are not lists of tuples
        ValueError: If points are not 2D coordinates
    """
    # Input validation
    if not isinstance(points_a, list) or not isinstance(points_b, list):
        raise TypeError("Inputs must be lists of points")
    
    # Handle empty list cases
    if not points_a or not points_b:
        return None
    
    # Validate point tuples
    for lst in [points_a, points_b]:
        for point in lst:
            if not isinstance(point, tuple) or len(point) != 2:
                raise ValueError("Points must be 2D tuples (x, y)")
            if not all(isinstance(coord, (int, float)) for coord in point):
                raise ValueError("Point coordinates must be numeric")
    
    # Initialize variables to track closest points
    min_distance = float('inf')
    closest_point_a = None
    closest_point_b = None
    
    # Compare every point in A with every point in B
    for point_a in points_a:
        for point_b in points_b:
            # Calculate Euclidean distance
            distance = math.sqrt(
                (point_a[0] - point_b[0])**2 + 
                (point_a[1] - point_b[1])**2
            )
            
            # Update if we find a closer pair
            if distance < min_distance:
                min_distance = distance
                closest_point_a = point_a
                closest_point_b = point_b
    
    return (closest_point_a, closest_point_b)