import random

def bogosort(arr):
    """
    Implement the bogosort (permutation sort) algorithm.
    
    Bogosort works by randomly shuffling the list until it becomes sorted.
    This is an extremely inefficient sorting algorithm with O(∞) time complexity.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: A sorted version of the input list
    """
    def is_sorted(lst):
        """Check if the list is sorted in ascending order."""
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Shuffle and check until sorted
    while not is_sorted(sorted_arr):
        random.shuffle(sorted_arr)
    
    return sorted_arr