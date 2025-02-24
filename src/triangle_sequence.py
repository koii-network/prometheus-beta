def generate_triangle_sequence(n):
    """
    Generate the first n numbers in a Triangle Number Sequence.
    
    A Triangle Number is a number that can be represented as a triangular grid of points
    where the first number is 1, and each subsequent number is the sum of the previous 
    triangular number and the current sequence number.
    
    Args:
        n (int): The number of triangle numbers to generate
    
    Returns:
        list: A list of the first n triangle numbers
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Number of triangle numbers must be non-negative")
    
    triangle_sequence = []
    for i in range(1, n + 1):
        # Triangle number formula: T(i) = i * (i + 1) // 2
        triangle_number = i * (i + 1) // 2
        triangle_sequence.append(triangle_number)
    
    return triangle_sequence