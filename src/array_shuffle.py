import random

def shuffle_array(arr):
    """
    Shuffles the elements of an input array randomly.
    
    Args:
        arr (list): The input array to be shuffled.
    
    Returns:
        list: A new list with elements randomly shuffled.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    shuffled = arr.copy()
    
    # Use Fisher-Yates (Knuth) shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled