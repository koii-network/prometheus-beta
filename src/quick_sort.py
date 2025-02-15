def quick_sort(arr):
    """
    Implement Quick Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    def partition(low, high):
        """
        Partition the list and return the pivot index.
        
        Args:
            low (int): Starting index of the partition.
            high (int): Ending index of the partition.
        
        Returns:
            int: The index of the pivot element.
        """
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Pointer for greater element
        i = low - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            if arr[j] <= pivot:
                # If element smaller than pivot is found
                # Swap it with the greater element pointed by i
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot element with the greater element specified by i
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        # Return the position from where partition is done
        return i + 1
    
    def quick_sort_recursive(low, high):
        """
        Recursive helper function to perform Quick Sort.
        
        Args:
            low (int): Starting index of the list or sublist.
            high (int): Ending index of the list or sublist.
        """
        if low < high:
            # Find pivot element such that 
            # elements smaller than pivot are on the left
            # elements greater than pivot are on the right
            pivot_index = partition(low, high)
            
            # Recursive call on the left of pivot
            quick_sort_recursive(low, pivot_index - 1)
            
            # Recursive call on the right of pivot
            quick_sort_recursive(pivot_index + 1, high)
    
    # Call the recursive helper function
    quick_sort_recursive(0, len(arr) - 1)
    
    return arr