def fibonacci(n):
    """
    Generate Fibonacci sequence up to a given number.
    
    Args:
        n (int): The maximum number in the Fibonacci sequence.
    
    Returns:
        list: Fibonacci sequence numbers less than or equal to n.
    """
    if n < 1:
        return []
    
    fib_seq = [1, 1]
    while True:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > n:
            break
        fib_seq.append(next_num)
    
    return fib_seq

def fibonacciSum(arr):
    """
    Calculate the sum of Fibonacci sequence up to the largest number in the input array.
    
    Args:
        arr (list): List of positive integers.
    
    Returns:
        int: Sum of Fibonacci sequence up to the largest number in the array.
    
    Raises:
        ValueError: If the input array is empty or contains non-positive integers.
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if any(num <= 0 for num in arr):
        raise ValueError("All numbers in the array must be positive integers")
    
    max_num = max(arr)
    fib_seq = fibonacci(max_num)
    
    return sum(fib_seq)