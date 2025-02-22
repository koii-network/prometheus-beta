import random

def shuffle_array(arr):
    """
    Shuffle the elements of an input array randomly.
    
    Args:
        arr (list): The input array to be shuffled
    
    Returns:
        list: A new list with the elements shuffled randomly
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    shuffled_arr = arr.copy()
    random.shuffle(shuffled_arr)
    return shuffled_arr