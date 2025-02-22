import random

def bogosort(arr):
    """
    Implement the bogosort (permutation sort) algorithm.
    
    This is an extremely inefficient sorting algorithm that randomly shuffles 
    the list until it becomes sorted. It has an average and worst-case time 
    complexity of O(∞) - it may never terminate for large lists.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: A sorted version of the input list
    """
    def is_sorted(lst):
        """Check if the list is sorted in ascending order."""
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Make a copy to avoid modifying the original list
    working_list = arr.copy()
    
    # Keep shuffling until the list is sorted
    while not is_sorted(working_list):
        # Randomly shuffle the list
        random.shuffle(working_list)
    
    return working_list