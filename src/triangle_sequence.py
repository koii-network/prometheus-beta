def generate_triangle_sequence(n):
    """
    Generate the first n numbers in a Triangle Number Sequence.

    A Triangle Number Sequence is a sequence where each number 
    represents the sum of consecutive integers from 1 to its position.
    For example: 1, 3, 6, 10, 15, ...

    Args:
        n (int): The number of triangle numbers to generate.

    Returns:
        list: A list of the first n triangle numbers.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of sequence elements must be non-negative")
    
    # Generate triangle sequence
    triangle_sequence = []
    for i in range(1, n + 1):
        # Triangle number formula: n * (n + 1) // 2
        triangle_number = i * (i + 1) // 2
        triangle_sequence.append(triangle_number)
    
    return triangle_sequence