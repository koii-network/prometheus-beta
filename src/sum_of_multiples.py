def sum_of_multiples(a: int, b: int) -> int:
    """
    Calculate the sum of all multiples of a and b in the range from 1 to 100.

    Args:
        a (int): First integer between 1 and 100
        b (int): Second integer between 1 and 100

    Returns:
        int: Sum of all unique multiples of a and b from 1 to 100

    Raises:
        ValueError: If a or b is not an integer between 1 and 100
    """
    # Validate input parameters
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both a and b must be integers")
    
    if not (1 <= a <= 100 and 1 <= b <= 100):
        raise ValueError("Both a and b must be between 1 and 100 (inclusive)")

    # Use a set to ensure unique multiples
    multiples = set()
    
    # Find multiples of a
    for num in range(a, 101, a):
        multiples.add(num)
    
    # Find multiples of b
    for num in range(b, 101, b):
        multiples.add(num)
    
    # Return the sum of unique multiples
    return sum(multiples)