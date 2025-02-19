def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all multiples of given numbers up to a limit.
    
    Args:
        limit (int): The upper limit (inclusive) for finding multiples.
        multiples (list): A list of integers to find multiples of.
    
    Returns:
        int: The sum of all unique multiples less than or equal to the limit.
    
    Raises:
        ValueError: If limit or any multiple is less than or equal to 0.
    """
    # Validate inputs
    if limit <= 0:
        raise ValueError("Limit must be a positive integer")
    
    if not multiples:
        return 0
    
    # Check if all multiples are positive
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers")
    
    # Use a set to store unique multiples
    unique_multiples = set()
    
    # Find all multiples for each number in the multiples list
    for multiple in multiples:
        for i in range(multiple, limit + 1, multiple):
            if i <= limit:
                unique_multiples.add(i)
    
    # Return the sum of unique multiples
    return sum(unique_multiples)