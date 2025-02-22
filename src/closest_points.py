import math
from typing import List, Tuple

def find_closest_points(list_a: List[Tuple[float, float]], 
                        list_b: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float], float]:
    """
    Find the two closest points between two lists of points in the Cartesian plane.
    
    Args:
        list_a (List[Tuple[float, float]]): First list of points (x, y coordinates)
        list_b (List[Tuple[float, float]]): Second list of points (x, y coordinates)
    
    Returns:
        Tuple containing:
        - Point from list_a
        - Point from list_b
        - Euclidean distance between the points
    
    Raises:
        ValueError: If either input list is empty
    """
    if not list_a or not list_b:
        raise ValueError("Both input lists must be non-empty")
    
    min_distance = float('inf')
    closest_point_a = None
    closest_point_b = None
    
    for point_a in list_a:
        for point_b in list_b:
            # Calculate Euclidean distance
            distance = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
            
            # Update minimum distance if a smaller distance is found
            if distance < min_distance:
                min_distance = distance
                closest_point_a = point_a
                closest_point_b = point_b
    
    return closest_point_a, closest_point_b, min_distance