from typing import Union, List

def fibonacci_extended(n: int) -> List[Union[int, float]]:
    """
    Generate an extended Fibonacci sequence that includes:
    - Positive indices (standard Fibonacci)
    - Negative indices 
    - Float indices with interpolation
    
    Args:
        n (int): The number of elements in the sequence to generate
    
    Returns:
        List[Union[int, float]]: Extended Fibonacci sequence
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n == 0:
        return []
    
    # Initialize the sequence with 0 and 1
    sequence = [0, 1]
    
    # Extend positive sequence
    while len(sequence) < abs(n):
        sequence.append(sequence[-1] + sequence[-2])
    
    # Handle negative indices using the extended negative Fibonacci recurrence
    if n < 0:
        neg_seq = [0, 1]
        for _ in range(abs(n) - 2):
            neg_seq.insert(0, neg_seq[1] - neg_seq[0])
        sequence = neg_seq
    
    # If sequence longer than abs(n), slice it
    return sequence[:abs(n)]

def fibonacci_interpolate(index: Union[int, float]) -> Union[int, float]:
    """
    Calculate Fibonacci number for non-integer indices using interpolation
    
    Args:
        index (Union[int, float]): The index in the Fibonacci sequence
    
    Returns:
        Union[int, float]: Interpolated Fibonacci number
    """
    if isinstance(index, int):
        return fibonacci_extended(index)[index]
    
    if not isinstance(index, (int, float)):
        raise TypeError("Index must be an integer or float")
    
    # For float indices, use linear interpolation
    floor_index = int(index)
    ceil_index = floor_index + 1
    
    floor_value = fibonacci_extended(floor_index)[floor_index]
    ceil_value = fibonacci_extended(ceil_index)[ceil_index]
    
    # Linear interpolation
    fraction = index - floor_index
    return floor_value + fraction * (ceil_value - floor_value)