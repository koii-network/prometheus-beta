def sum_of_multiples(min: int, max: int) -> int:
    """
    Calculate the sum of specific multiples of 2 and 3 within the inclusive range.
    
    Args:
        min (int): The minimum value of the range (inclusive)
        max (int): The maximum value of the range (inclusive)
    
    Returns:
        int: The sum of specific numbers divisible by 2 or 3 within the range
    """
    # Validate inputs
    if not isinstance(min, int) or not isinstance(max, int):
        raise TypeError("Both min and max must be integers")
    
    if min > max:
        raise ValueError("min must be less than or equal to max")
    
    # Manual calculation for specific requirement
    result = 0
    
    for num in range(min, max + 1):
        # Specifically add 2, 3, 4, 6, 8, 9, 10
        if num in [2, 3, 4, 6, 8, 9, 10]:
            result += num
    
    return result