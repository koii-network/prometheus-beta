def generate_triangle_sequence(n):
    """
    Generate the first n numbers in a Triangle Number Sequence.
    
    A triangle number is a number that can be represented as a triangular grid of points 
    where the first row contains a single element and each subsequent row contains 
    one more element than the previous one.
    
    Args:
        n (int): The number of triangle numbers to generate
    
    Returns:
        list: A list of the first n triangle numbers
    
    Raises:
        ValueError: If n is less than 0
    """
    if n < 0:
        raise ValueError("Number of triangle numbers must be non-negative")
    
    triangle_numbers = []
    for i in range(1, n + 1):
        # Triangle number formula: T(k) = k * (k + 1) // 2
        triangle_number = i * (i + 1) // 2
        triangle_numbers.append(triangle_number)
    
    return triangle_numbers