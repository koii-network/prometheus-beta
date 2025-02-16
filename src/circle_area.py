import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle (must be non-negative)
    
    Returns:
        float: The area of the circle
    
    Raises:
        ValueError: If radius is negative
        TypeError: If radius is not a number
    """
    # Check if radius is a number
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    
    # Check if radius is non-negative
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    # Calculate and return the area using pi * r^2
    return math.pi * radius ** 2