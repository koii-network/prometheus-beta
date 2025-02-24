from typing import List

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    This function uses a recursive approach to create the Fibonacci sequence
    with O(n) time complexity and without using explicit loops.
    
    Args:
        n (int): The number of Fibonacci sequence elements to generate.
               Must be a non-negative integer.
    
    Returns:
        List[int]: A list containing the first n numbers of the Fibonacci sequence.
    
    Raises:
        ValueError: If n is a negative integer.
    
    Examples:
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case handling
    if n == 0:
        return []
    
    def fib_helper(count: int) -> List[int]:
        """
        Recursive helper function to generate Fibonacci sequence.
        
        Args:
            count (int): Number of Fibonacci numbers to generate.
        
        Returns:
            List[int]: List of Fibonacci numbers.
        """
        if count <= 0:
            return []
        if count == 1:
            return [0]
        if count == 2:
            return [0, 1]
        
        # Recursively generate the sequence
        prev_seq = fib_helper(count - 1)
        next_num = prev_seq[-1] + prev_seq[-2]
        return prev_seq + [next_num]
    
    return fib_helper(n)