def sum_of_multiples(min: int, max: int) -> int:
    """
    Calculate the sum of all unique multiples of 2 and 3 within the inclusive range.
    
    Args:
        min (int): The minimum value of the range (inclusive)
        max (int): The maximum value of the range (inclusive)
    
    Returns:
        int: The sum of all unique numbers divisible by 2 or 3 within the range
    """
    # Validate inputs
    if not isinstance(min, int) or not isinstance(max, int):
        raise TypeError("Both min and max must be integers")
    
    if min > max:
        raise ValueError("min must be less than or equal to max")
    
    # Sum unique multiples in a single pass
    unique_multiples_sum = sum(
        num for num in range(min, max + 1) 
        if num % 2 == 0 or num % 3 == 0
    )
    
    return unique_multiples_sum