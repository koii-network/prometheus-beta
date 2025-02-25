def calculate_rectangle_perimeter(length: float, width: float) -> float:
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.

    Raises:
        ValueError: If length or width is negative.
        TypeError: If length or width is not a number.
    """
    # Validate input types
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise TypeError("Length and width must be numeric values")
    
    # Validate non-negative inputs
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    # Calculate perimeter: 2 * (length + width)
    return 2 * (length + width)