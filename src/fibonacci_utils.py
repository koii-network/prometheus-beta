def fibonacci(n):
    """
    Generate Fibonacci sequence up to a given number.
    
    Args:
        n (int): The maximum number in the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci numbers less than or equal to n.
    
    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n < 2:
        return [0] if n == 0 else [0, 1]
    
    fib_seq = [0, 1]
    while True:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > n:
            break
        fib_seq.append(next_num)
    
    return fib_seq

def fibonacci_sum(arr):
    """
    Calculate the sum of Fibonacci sequence up to the largest number in the input array.
    
    Args:
        arr (list): A list of non-negative integers.
    
    Returns:
        int: Sum of Fibonacci numbers up to the maximum value in the input array.
    
    Raises:
        ValueError: If the input is not a list of integers.
    """
    # Validate input
    if not arr:
        return 0
    
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("Input must be a list of non-negative integers")
    
    # Find the maximum number to generate Fibonacci sequence
    max_num = max(arr)
    
    # Generate Fibonacci sequence and sum it
    return sum(fibonacci(max_num))