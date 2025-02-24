def count_factors(n: int) -> int:
    """
    Count the number of factors for a given positive integer.

    Args:
        n (int): A positive integer to count factors for.

    Returns:
        int: The total number of factors of the input number.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Count factors
    factor_count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # If divisors are different, count both
            if i * i == n:
                factor_count += 1
            else:
                factor_count += 2
    
    return factor_count