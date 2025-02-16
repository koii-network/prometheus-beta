def tournament_sort(arr):
    """
    Implement tournament sort algorithm.
    
    Tournament sort works by creating a binary tournament tree to sort elements.
    It has a time complexity of O(n log n) and is less memory-efficient than 
    traditional sorting algorithms like merge sort or quicksort.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list 
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    working_list = arr.copy()
    
    # Create the initial tournament tree
    def create_tournament_tree(elements):
        if len(elements) == 1:
            return elements[0]
        
        # Split the list into two halves
        mid = len(elements) // 2
        left = elements[:mid]
        right = elements[mid:]
        
        # Recursively create tournament tree
        left_winner = create_tournament_tree(left)
        right_winner = create_tournament_tree(right)
        
        # Return the winner (smaller element)
        return min(left_winner, right_winner)
    
    # Perform the tournament sort
    sorted_list = []
    while working_list:
        # Find the winner of the tournament
        winner = create_tournament_tree(working_list)
        
        # Add winner to sorted list
        sorted_list.append(winner)
        
        # Remove the winner from working list
        working_list.remove(winner)
    
    return sorted_list