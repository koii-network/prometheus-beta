def generate_triangle_sequence(n):
    """
    Generate the first n numbers in a Triangle Number Sequence.
    
    A triangle number is a number that can be represented as a triangular grid of points 
    where the first row contains a single element and each subsequent row contains 
    one more element than the previous one.
    
    Formula: Triangle Number = n * (n + 1) // 2
    
    Args:
        n (int): Number of triangle numbers to generate
    
    Returns:
        list: A list of the first n triangle numbers
    
    Raises:
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of triangle numbers must be non-negative")
    
    return [i * (i + 1) // 2 for i in range(n)]