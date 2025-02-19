def fibonacci(n):
    """
    Generate Fibonacci sequence up to a given number.
    
    :param n: Upper limit for Fibonacci sequence
    :return: List of Fibonacci numbers less than or equal to n
    """
    if n < 1:
        return []
    
    fib_seq = [1]
    last_num = 1
    
    while last_num <= n:
        if last_num == 1 and last_num < n:
            last_num = 1  # Explicitly add a second 1
        else:
            last_num = fib_seq[-1] + (fib_seq[-2] if len(fib_seq) > 1 else 0)
        
        if last_num > n:
            break
        
        fib_seq.append(last_num)
    
    return fib_seq

def fibonacciSum(arr):
    """
    Calculate the sum of Fibonacci sequence up to the largest number in the array.
    
    :param arr: List of positive integers
    :return: Sum of Fibonacci sequence
    :raises ValueError: If input is not a list of positive integers
    """
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    max_num = max(arr)
    fib_sequence = fibonacci(max_num)
    
    return sum(fib_sequence)