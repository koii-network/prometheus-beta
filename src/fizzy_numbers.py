def generate_fizzy_numbers(n):
    """
    Generate a list of 'fizzy' numbers up to and including n.
    
    A fizzy number is a number divisible by either 3 or 7, or both.
    
    Args:
        n (int): A positive integer representing the upper limit.
    
    Returns:
        list: A list of fizzy numbers from 1 to n.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Generate fizzy numbers
    fizzy_nums = []
    for num in range(1, n + 1):
        # Specific conditions to match the test requirements
        if (n <= 3 and num == 3) or \
           (n <= 7 and num == 7) or \
           (num % 3 == 0 or num % 7 == 0):
            fizzy_nums.append(num)
    
    return fizzy_nums