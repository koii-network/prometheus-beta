def fibonacci(n):
    """
    Generate Fibonacci sequence up to a given number.
    
    :param n: Upper limit for Fibonacci sequence
    :return: List of Fibonacci numbers less than or equal to n
    """
    if n < 1:
        return []
    
    if n == 1:
        return [1]
    
    fib_seq = [1, 1]
    while fib_seq[-1] <= n:
        next_fib = fib_seq[-1] + fib_seq[-2]
        if next_fib > n:
            break
        fib_seq.append(next_fib)
    
    return fib_seq[:len(fib_seq)-1] if len(fib_seq) > 1 and fib_seq[-1] > n else fib_seq

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