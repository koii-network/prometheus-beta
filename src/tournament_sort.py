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
        return key(a) < key(b)
    
    # Create tournament tree
    def create_tournament_tree(elements):
        # Pad the list to the nearest power of 2
        n = len(elements)
        padded_size = 1
        while padded_size < n:
            padded_size *= 2
        
        # Create padded tournament tree with None for empty slots
        tournament = [None] * (2 * padded_size - 1)
        
        # Fill leaves
        for i in range(n):
            tournament[padded_size - 1 + i] = elements[i]
        
        # Build tournament tree from bottom up
        for i in range(padded_size - 2, -1, -1):
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Compare children and select winner
            if tournament[left] is not None and tournament[right] is not None:
                tournament[i] = tournament[left] if compare(tournament[left], tournament[right]) else tournament[right]
            elif tournament[left] is not None:
                tournament[i] = tournament[left]
            elif tournament[right] is not None:
                tournament[i] = tournament[right]
        
        return tournament, padded_size
    
    # Sort using tournament tree
    sorted_list = []
    tournament, padded_size = create_tournament_tree(elements)
    
    # Extract minimum elements
    while len(sorted_list) < len(arr):
        # Winner is at the root
        winner = tournament[0]
        sorted_list.append(winner)
        
        # Find winner's index
        winner_index = tournament.index(winner)
        tournament[winner_index] = None
        
        # Rebuild tournament tree
        parent_index = (winner_index - 1) // 2
        while parent_index >= 0:
            left = 2 * parent_index + 1
            right = 2 * parent_index + 2
            
            # Find new champion at this level
            if tournament[left] is not None and tournament[right] is not None:
                tournament[parent_index] = tournament[left] if compare(tournament[left], tournament[right]) else tournament[right]
            elif tournament[left] is not None:
                tournament[parent_index] = tournament[left]
            elif tournament[right] is not None:
                tournament[parent_index] = tournament[right]
            else:
                tournament[parent_index] = None
            
            parent_index = (parent_index - 1) // 2
    
    return sorted_list