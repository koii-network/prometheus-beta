def sum_of_multiples(a: int, b: int) -> int:
    """
    Calculate the sum of all multiples of a and b in the range from 1 to 100.
    
    Args:
        a (int): First number to find multiples of (1 <= a <= 100)
        b (int): Second number to find multiples of (1 <= b <= 100)
    
    Returns:
        int: Sum of all unique multiples of a and b from 1 to 100
    
    Raises:
        ValueError: If a or b are not integers between 1 and 100
    """
    # Validate input
    if not (1 <= a <= 100 and 1 <= b <= 100):
        raise ValueError("Both a and b must be integers between 1 and 100")
    
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