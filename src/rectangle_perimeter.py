def calculate_rectangle_perimeter(length: float, width: float) -> float:
    """
    Calculate the perimeter of a rectangle given its length and width.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The perimeter of the rectangle
    
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers")
    
    return 2 * (length + width)