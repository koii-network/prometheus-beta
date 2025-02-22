def extended_fibonacci(n):
    """
    Generate the nth number in the extended Fibonacci sequence, supporting 
    negative indices and floating-point values.
    
    Args:
        n (int or float): The index of the Fibonacci number to generate.
    
    Returns:
        float: The Fibonacci number at the given index.
    """
    # Handle special cases
    if n == 0:
        return 0
    if n == 1 or n == -1:
        return 1
    
    # Separate integer part and sign
    is_negative = n < 0
    abs_n = abs(n)
    
    # Use memoization for efficiency
    memo = {0: 0, 1: 1, -1: 1}
    
    # Helper function for computing Fibonacci for positive indices
    def fib(k):
        if k in memo:
            return memo[k]
        
        # Handle floating-point indices using linear interpolation
        if isinstance(k, float):
            floor_k = int(k)
            ceil_k = floor_k + 1
            floor_value = fib(floor_k)
            ceil_value = fib(ceil_k)
            fraction = k - floor_k
            interpolated_value = floor_value + fraction * (ceil_value - floor_value)
            memo[k] = interpolated_value
            return interpolated_value
        
        # Recursive calculation for integer indices
        result = fib(k - 1) + fib(k - 2)
        memo[k] = result
        return result
    
    # Compute the value and adjust sign for negative indices
    result = fib(abs_n)
    return result if not is_negative else ((-1)**(abs_n+1)) * result