def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of given numbers up to a limit.
    
    Args:
        limit (int): The upper bound (inclusive) for finding multiples.
        multiples (list): A list of integers to find multiples of.
    
    Returns:
        int: Sum of unique multiples less than or equal to the limit.
    
    Raises:
        ValueError: If limit or any multiple is less than or equal to 0.
    """
    # Validate input
    if limit <= 0:
        raise ValueError("Limit must be a positive integer")
    
    if not multiples:
        return 0
    
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers")
    
    # Use a set to ensure unique multiples
    unique_multiples = set()
    
    # Find all unique multiples
    for multiple in multiples:
        for num in range(multiple, limit + 1, multiple):
            if num <= limit:
                unique_multiples.add(num)
    
    # Return the sum of unique multiples
    return sum(unique_multiples)