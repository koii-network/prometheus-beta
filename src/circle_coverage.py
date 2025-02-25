import math
from typing import List, Tuple

class Circle:
    def __init__(self, x: float, y: float, radius: float):
        """
        Represents a circle with a center point and radius.
        
        Args:
            x (float): x-coordinate of the circle's center
            y (float): y-coordinate of the circle's center
            radius (float): radius of the circle
        """
        self.x = x
        self.y = y
        self.radius = radius

def calculate_distance(circle1: Circle, circle2: Circle) -> float:
    """
    Calculate the Euclidean distance between the centers of two circles.
    
    Args:
        circle1 (Circle): First circle
        circle2 (Circle): Second circle
    
    Returns:
        float: Distance between circle centers
    """
    return math.sqrt((circle1.x - circle2.x)**2 + (circle1.y - circle2.y)**2)

def do_circles_overlap(circle1: Circle, circle2: Circle) -> bool:
    """
    Check if two circles overlap.
    
    Args:
        circle1 (Circle): First circle
        circle2 (Circle): Second circle
    
    Returns:
        bool: True if circles overlap, False otherwise
    """
    distance = calculate_distance(circle1, circle2)
    return distance < circle1.radius + circle2.radius

def min_circle_coverage(circles: List[Circle]) -> List[Circle]:
    """
    Find the minimum number of circles to cover all input circles without overlap.
    
    Args:
        circles (List[Circle]): List of input circles to be covered
    
    Returns:
        List[Circle]: Minimal set of covering circles
    
    Raises:
        ValueError: If input list is empty
    """
    if not circles:
        raise ValueError("Input list of circles cannot be empty")
    
    # If only one circle, return it
    if len(circles) == 1:
        return circles.copy()
    
    # Sort circles by radius in descending order for greedy coverage
    sorted_circles = sorted(circles, key=lambda c: c.radius, reverse=True)
    covered_circles = set()
    covering_circles = []
    
    for circle in sorted_circles:
        # Check if this circle is completely alone (not overlapping)
        if all(not do_circles_overlap(circle, other_circle) for other_circle in sorted_circles if other_circle != circle):
            covering_circles.append(circle)
        else:
            # Check if this circle can cover other circles
            if not any(circle in covered_circles for circle in covered_circles):
                covering_circles.append(circle)
                
                # Mark this and overlapping circles as covered
                for other_circle in sorted_circles:
                    if do_circles_overlap(circle, other_circle):
                        covered_circles.add(other_circle)
    
    return covering_circles