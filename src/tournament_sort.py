from typing import List, TypeVar, Callable

T = TypeVar('T')

def tournament_sort(arr: List[T], compare: Callable[[T, T], bool] = lambda x, y: x < y) -> List[T]:
    """
    Implement tournament sort algorithm.
    
    Tournament sort is a sorting algorithm that uses a tournament tree (binary heap) 
    to sort elements efficiently.
    
    Args:
        arr (List[T]): The input list to be sorted
        compare (Callable[[T, T], bool], optional): Comparison function. 
            Defaults to ascending order (less than comparison)
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Cannot sort an empty list")
    
    # If list has only one element, return it
    if len(arr) == 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    working_arr = arr.copy()
    
    # Build tournament tree (winner's bracket)
    def tournament(start: int, end: int) -> int:
        """
        Create a tournament tree and return the winner's index
        
        Args:
            start (int): Starting index of the tournament
            end (int): Ending index of the tournament
        
        Returns:
            int: Index of the winner
        """
        # Base case: single element
        if start == end:
            return start
        
        # If only two elements, compare and return winner
        if end - start == 1:
            return start if compare(working_arr[start], working_arr[end]) else end
        
        # Divide and conquer
        mid = (start + end) // 2
        left_winner = tournament(start, mid)
        right_winner = tournament(mid + 1, end)
        
        # Compare winners
        return left_winner if compare(working_arr[left_winner], working_arr[right_winner]) else right_winner
    
    # Create output list
    sorted_arr = []
    
    # Repeat until all elements are sorted
    while len(working_arr) > 0:
        # Find tournament winner
        winner_index = tournament(0, len(working_arr) - 1)
        
        # Add winner to sorted list
        sorted_arr.append(working_arr.pop(winner_index))
    
    return sorted_arr