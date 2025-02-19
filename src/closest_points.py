import math
from typing import List, Tuple

def find_closest_points(A: List[Tuple[float, float]], B: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float], float]:
    """
    Find the two closest points, one from list A and one from list B.
    
    :param A: List of points in the first set, each point is a (x, y) tuple
    :param B: List of points in the second set, each point is a (x, y) tuple
    :return: A tuple containing the closest point from A, closest point from B, and their Euclidean distance
    
    :raises ValueError: If either input list is empty
    """
    # Input validation
    if not A or not B:
        raise ValueError("Both input lists must be non-empty")
    
    # Initialize minimum distance to a large value
    min_distance = float('inf')
    closest_point_a = None
    closest_point_b = None
    
    # Compute Euclidean distance between all points in A and B
    for point_a in A:
        for point_b in B:
            # Calculate Euclidean distance
            distance = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
            
            # Update minimum distance and closest points if a smaller distance is found
            if distance < min_distance:
                min_distance = distance
                closest_point_a = point_a
                closest_point_b = point_b
    
    return closest_point_a, closest_point_b, min_distance