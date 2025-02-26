def find_fizzy_numbers(n):
    """
    Find and return all 'fizzy' numbers up to and including n.
    
    A fizzy number is a number divisible by either 3 or 7, or both.
    
    Args:
        n (int): A positive integer upper limit for finding fizzy numbers.
    
    Returns:
        list: A sorted list of fizzy numbers from 1 to n.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Find fizzy numbers
    fizzy_numbers = [
        num for num in range(1, n + 1) 
        if num % 3 == 0 or num % 7 == 0
    ]
    
    return fizzy_numbers