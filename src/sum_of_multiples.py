def sum_of_multiples(a: int, b: int) -> int:
    """
    Calculate the sum of all multiples of a and b in the range from 1 to 100 (inclusive).
    
    Args:
        a (int): First integer to find multiples of (between 1 and 100)
        b (int): Second integer to find multiples of (between 1 and 100)
    
    Returns:
        int: Sum of all unique multiples of a and b in the range 1 to 100
    
    Raises:
        ValueError: If a or b is less than 1 or greater than 100
    """
    # Validate input parameters
    if not (1 <= a <= 100 and 1 <= b <= 100):
        raise ValueError("Both a and b must be integers between 1 and 100 (inclusive)")
    
    # Use a set to avoid counting duplicate multiples
    multiples = set()
    
    # Find multiples of a
    for i in range(a, 101, a):
        multiples.add(i)
    
    # Find multiples of b
    for i in range(b, 101, b):
        multiples.add(i)
    
    # Return the sum of unique multiples
    return sum(multiples)