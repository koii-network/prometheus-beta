def sum_of_multiples(min: int, max: int) -> int:
    """
    Calculate the sum of all multiples of 2 and 3 within the inclusive range.
    
    Args:
        min (int): The minimum value of the range (inclusive)
        max (int): The maximum value of the range (inclusive)
    
    Returns:
        int: The sum of all numbers divisible by 2 or 3 within the range
    """
    # Validate inputs
    if not isinstance(min, int) or not isinstance(max, int):
        raise TypeError("Both min and max must be integers")
    
    if min > max:
        raise ValueError("min must be less than or equal to max")
    
    # Use a set to avoid counting the same number multiple times
    multiples = set()
    
    # Add multiples of 2
    for num in range(min, max + 1):
        if num % 2 == 0:
            multiples.add(num)
    
    # Add multiples of 3
    for num in range(min, max + 1):
        if num % 3 == 0:
            multiples.add(num)
    
    # Return the sum of unique multiples
    return sum(multiples)