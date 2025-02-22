def spaghetti_sort(arr):
    """
    Implement the Spaghetti Sort (Strand Sort) algorithm.
    
    This algorithm works by repeatedly extracting sorted sublists from the input 
    and merging them to create a fully sorted list.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy of the input list to work with
    working_list = arr.copy()
    sorted_list = []
    
    while working_list:
        # Extract the first element as the initial sublist
        sublist = [working_list.pop(0)]
        
        # Go through remaining elements
        i = 0
        while i < len(working_list):
            # If current element is greater than the last element in sublist, 
            # it can be added to sublist
            if working_list[i] >= sublist[-1]:
                sublist.append(working_list.pop(i))
            else:
                i += 1
        
        # Merge the extracted sublist with the sorted list
        sorted_list = merge(sorted_list, sublist)
    
    return sorted_list

def merge(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    
    Returns:
        list: Merged sorted list
    """
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements from list1, if any
    merged.extend(list1[i:])
    
    # Add remaining elements from list2, if any
    merged.extend(list2[j:])
    
    return merged