def strand_sort(arr):
    """
    Implement the strand sort algorithm to sort a list.
    
    Strand sort works by repeatedly extracting sorted sublists 
    and merging them together.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a working copy of the input list
    working = arr.copy()
    result = []
    
    while working:
        # Extract the first sublist
        sublist = [working.pop(0)]
        
        # Iterate through remaining elements to create sorted sublist
        i = 0
        while i < len(working):
            # If current element is greater than last element in sublist, add it
            if working[i] > sublist[-1]:
                sublist.append(working.pop(i))
            else:
                i += 1
        
        # Merge the extracted sublist with the result
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