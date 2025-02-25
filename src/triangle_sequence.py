def generate_triangle_sequence(n):
    """
    Generate the first n numbers in the Triangle Number Sequence.

    A Triangle Number Sequence is a sequence where each number is the sum of 
    consecutive integers from 1 to k. For example:
    1st triangle number: 1
    2nd triangle number: 1 + 2 = 3
    3rd triangle number: 1 + 2 + 3 = 6
    4th triangle number: 1 + 2 + 3 + 4 = 10

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
        raise TypeError("Input must be a non-negative integer")
    
    if n < 0:
        raise ValueError("Number of triangle numbers must be non-negative")
    
    # Generate triangle sequence
    triangle_sequence = []
    current_sum = 0
    
    for k in range(1, n + 1):
        current_sum += k
        triangle_sequence.append(current_sum)
    
    return triangle_sequence