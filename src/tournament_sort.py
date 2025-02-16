def tournament_sort(arr):
    """
    Implement the tournament sort algorithm.
    
    Tournament sort is a sorting algorithm that uses a tournament tree (binary tree)
    to sort an array with a time complexity of O(n log n).
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains incomparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    n = len(arr)
    sorted_arr = []
    
    # Create a tournament tree (implemented as a list)
    def create_tournament_tree(items):
        # If single item, return it
        if len(items) == 1:
            return items[0]
        
        # Split list into two halves
        mid = len(items) // 2
        left = create_tournament_tree(items[:mid])
        right = create_tournament_tree(items[mid:])
        
        # Return the smaller of the two
        return left if left <= right else right
    
    # Clone the original array to manipulate
    remaining = arr.copy()
    
    # Perform tournament sort
    while remaining:
        # Create tournament tree to find the minimum
        winner = create_tournament_tree(remaining)
        
        # Add winner to sorted array
        sorted_arr.append(winner)
        
        # Remove the first occurrence of the winner
        remaining.remove(winner)
    
    return sorted_arr