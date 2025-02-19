import math
from typing import List, Tuple

def find_closest_points(list_a: List[Tuple[float, float]], list_b: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float], float]:
    """
    Find the two closest points, one from list A and one from list B.
    
    Args:
        list_a (List[Tuple[float, float]]): First list of points (x, y coordinates)
        list_b (List[Tuple[float, float]]): Second list of points (x, y coordinates)
    
    Returns:
        Tuple containing:
        - Point from list A
        - Point from list B
        - Euclidean distance between these points
    
    Raises:
        ValueError: If either input list is empty
    """
    # Check for empty lists
    if not list_a or not list_b:
        raise ValueError("Both input lists must contain at least one point")
    
    # Initialize minimum distance to a large value
    min_distance = float('inf')
    closest_point_a = None
    closest_point_b = None
    
    # Nested loop to compare each point in list A with each point in list B
    for point_a in list_a:
        for point_b in list_b:
            # Calculate Euclidean distance
            distance = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
            
            # Update minimum distance if a closer pair is found
            if distance < min_distance:
                min_distance = distance
                closest_point_a = point_a
                closest_point_b = point_b
    
    return closest_point_a, closest_point_b, min_distance