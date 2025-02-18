def strand_sort(arr):
    """
    Implement the strand sort algorithm to sort a list.
    
    Strand sort works by:
    1. Extracting a sorted sublist from the input list
    2. Merging this sublist with the result list
    3. Repeating until the input list is empty
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    remaining = arr.copy()
    result = []
    
    while remaining:
        # Extract the first element as the start of a sublist
        sublist = [remaining.pop(0)]
        
        # Go through the remaining list to extract elements in increasing order
        i = 0
        while i < len(remaining):
            # If the current element is greater than the last element in sublist, 
            # add it to the sublist and remove from remaining
            if remaining[i] > sublist[-1]:
                sublist.append(remaining.pop(i))
            else:
                i += 1
        
        # Merge the sublist with the result list
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