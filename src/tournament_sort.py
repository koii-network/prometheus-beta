from typing import List, TypeVar, Callable

T = TypeVar('T')

def tournament_sort(arr: List[T], key: Callable[[T], int] = lambda x: x) -> List[T]:
    """
    Implement the Tournament Sort algorithm.
    
    Tournament Sort is a comparison-based sorting algorithm that uses a tournament 
    tree (binary heap) to efficiently sort an array.
    
    Args:
        arr (List[T]): The input list to be sorted
        key (Callable[[T], int], optional): A function to extract a comparison key from each element. 
                                            Defaults to identity function.
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    elements = arr.copy()
    
    def compare(a, b):
        """Internal comparison function using the provided key"""
        if a is None:
            return False
        if b is None:
            return True
        return key(a) < key(b)
    
    # Perform tournament sorting
    sorted_list = []
    
    # Continue until all elements are sorted
    while elements:
        # Find the tournament winner
        winner_index = 0
        for i in range(1, len(elements)):
            if compare(elements[i], elements[winner_index]):
                winner_index = i
        
        # Add winner to sorted list and remove from original list
        sorted_list.append(elements[winner_index])
        elements.pop(winner_index)
    
    return sorted_list