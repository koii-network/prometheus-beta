def fibonacci(n):
    """
    Generate the Fibonacci sequence up to a given number.
    
    Args:
        n (int): The maximum number in the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci numbers less than or equal to n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0:
        return []
    
    fib_sequence = [1, 1]
    
    while fib_sequence[-1] <= n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    
    return fib_sequence

def fibonacci_sum(numbers):
    """
    Calculate the sum of Fibonacci numbers up to the largest number in the input array.
    
    Args:
        numbers (list): A list of positive integers.
    
    Returns:
        int: The sum of Fibonacci numbers up to the largest number in the input.
    
    Raises:
        ValueError: If the input is not a list or contains non-positive numbers.
    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of positive integers")
    
    if not numbers:
        return 0
    
    if any(not isinstance(num, int) or num <= 0 for num in numbers):
        raise ValueError("All numbers must be positive integers")
    
    max_num = max(numbers)
    fib_seq = fibonacci(max_num)
    
    return sum(fib_seq)