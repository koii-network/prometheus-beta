def sum_of_multiples(min: int, max: int) -> int:
    """
    Calculate the sum of all multiples of 2 and 3 within the given inclusive range.
    
    Args:
        min (int): The lower bound of the range (inclusive)
        max (int): The upper bound of the range (inclusive)
    
    Returns:
        int: Sum of all numbers in the range divisible by 2 or 3
    """
    # Using set to avoid counting numbers divisible by both 2 and 3 twice
    multiples = set()
    
    # Add multiples of 2
    for num in range(min, max + 1):
        if num % 2 == 0:
            multiples.add(num)
    
    # Add multiples of 3
    for num in range(min, max + 1):
        if num % 3 == 0:
            multiples.add(num)
    
    return sum(multiples)