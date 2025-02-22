import random

def shuffle_array(arr):
    """
    Shuffle the elements of an input array randomly.
    
    Args:
        arr (list): The input array to be shuffled.
    
    Returns:
        list: A new list with elements shuffled randomly.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the list to avoid modifying the original
    shuffled = arr.copy()
    
    # Use Fisher-Yates (Knuth) shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        
        # Swap elements
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled