def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of given numbers up to a limit.
    
    Args:
        limit (int): The upper bound (inclusive) for finding multiples.
        multiples (list): List of numbers to find multiples of.
    
    Returns:
        int: Sum of unique multiples not exceeding the limit.
    
    Raises:
        ValueError: If limit or any multiple is less than or equal to 0.
    """
    # Validate inputs
    if limit <= 0:
        raise ValueError("Limit must be a positive integer")
    
    if not multiples:
        return 0
    
    # Check if any multiple is non-positive
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers")
    
    # Collect unique multiples
    unique_multiples = set()
    
    # Find all multiples for each number in the multiples list
    for multiple in multiples:
        for i in range(multiple, limit + 1, multiple):
            unique_multiples.add(i)
    
    # Return the sum of unique multiples
    return sum(unique_multiples)