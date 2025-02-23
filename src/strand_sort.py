def strand_sort(arr):
    """
    Implement the Strand Sort algorithm to sort a list in ascending order.
    
    Strand Sort works by repeatedly extracting sorted sublists from the input 
    list and merging them together to create a fully sorted list.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    unsorted = arr.copy()
    result = []
    
    while unsorted:
        # Extract the first element as the initial sublist
        sublist = [unsorted.pop(0)]
        
        # Iterate through the remaining unsorted elements
        i = 0
        while i < len(unsorted):
            # If the current element is greater than the last element in sublist, 
            # add it to the sublist and remove from unsorted
            if unsorted[i] > sublist[-1]:
                sublist.append(unsorted.pop(i))
            else:
                i += 1
        
        # Merge the current sublist with the result list
        result = merge(result, sublist)
    
    return result

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
    
    # Compare and merge elements from both lists
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