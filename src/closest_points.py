import math
from typing import List, Tuple

def find_closest_points(A: List[Tuple[float, float]], B: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float], float]:
    """
    Find the two closest points between two lists of points in the Cartesian plane.
    
    Args:
        A (List[Tuple[float, float]]): First list of points (x, y coordinates)
        B (List[Tuple[float, float]]): Second list of points (x, y coordinates)
    
    Returns:
        Tuple containing:
        - The closest point from list A
        - The closest point from list B
        - The Euclidean distance between these points
    
    Raises:
        ValueError: If either input list is empty
    """
    # Input validation
    if not A or not B:
        raise ValueError("Both input lists must be non-empty")
    
    # Initialize minimum distance and corresponding points
    min_distance = float('inf')
    closest_point_a = A[0]
    closest_point_b = B[0]
    
    # Nested loops to compare all points between the two lists
    for point_a in A:
        for point_b in B:
            # Calculate Euclidean distance
            distance = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
            
            # Update minimum distance if a smaller distance is found
            if distance < min_distance:
                min_distance = distance
                closest_point_a = point_a
                closest_point_b = point_b
    
    return closest_point_a, closest_point_b, min_distance