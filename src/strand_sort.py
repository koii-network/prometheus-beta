def strand_sort(arr):
    """
    Implement the strand sort algorithm to sort a list.
    
    Strand sort works by:
    1. Extracting a sorted sublist from the input list
    2. Merging it with the result list
    3. Repeating until the input list is empty
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    """
    if not arr:
        return []
    
    result = []
    
    while arr:
        # Extract a sorted sublist
        sublist = [arr.pop(0)]
        i = 0
        
        while i < len(arr):
            # If the current element is greater than the last element of sublist,
            # add it to the sublist and remove from original list
            if arr[i] >= sublist[-1]:
                sublist.append(arr.pop(i))
            else:
                i += 1
        
        # Merge the extracted sublist with the result
        result = merge(result, sublist)
    
    return result

def merge(list1, list2):
    """
    Merge two sorted lists.
    
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
    
    # Add remaining elements from list1 or list2
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged