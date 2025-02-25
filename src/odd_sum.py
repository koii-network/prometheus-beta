def sum_odd_numbers(n):
    """
    Calculate the sum of all odd numbers between 1 and n (inclusive).
    
    Args:
        n (int): The upper limit of the range to sum odd numbers.
    
    Returns:
        int: The sum of all odd numbers from 1 to n.
    
    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.
    
    Time complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    return sum(num for num in range(1, n + 1) if num % 2 != 0)