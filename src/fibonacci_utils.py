def fibonacci(max_num):
    """
    Generate Fibonacci sequence up to a given maximum number.
    
    Args:
        max_num (int): The maximum number to generate Fibonacci sequence up to.
    
    Returns:
        list: A list of Fibonacci numbers less than or equal to max_num.
    
    Raises:
        ValueError: If max_num is negative.
    """
    if max_num < 0:
        raise ValueError("Maximum number must be non-negative")
    
    # Handle special cases
    if max_num == 0:
        return []
    if max_num == 1:
        return [1]
    if max_num == 2:
        return [1, 1, 2]
    
    # Generate Fibonacci sequence
    fib_seq = [1, 1]
    while True:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > max_num:
            break
        fib_seq.append(next_num)
    
    # Return sequence with numbers less than or equal to max_num
    return [num for num in fib_seq if num <= max_num]

def fibonacci_sum(arr):
    """
    Calculate the sum of Fibonacci numbers up to the largest number in the input array.
    
    Args:
        arr (list): A list of positive integers.
    
    Returns:
        int: The sum of Fibonacci numbers up to the largest number in the array.
    
    Raises:
        ValueError: If the input array is empty or contains non-positive numbers.
    """
    # Validate input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Check for non-positive numbers
    if any(num <= 0 for num in arr):
        raise ValueError("All numbers in the array must be positive")
    
    # Find the maximum number in the array
    max_num = max(arr)
    
    # Generate Fibonacci sequence up to max_num
    fib_sequence = fibonacci(max_num)
    
    # Return the sum of Fibonacci numbers
    return sum(set(fib_sequence))