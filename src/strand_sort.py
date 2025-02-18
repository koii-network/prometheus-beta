def strand_sort(arr):
    """
    Implement the Strand Sort algorithm to sort a list in ascending order.
    
    Strand Sort works by:
    1. Extracting a sorted sublist from the input list
    2. Merging the extracted sublist with the result list
    3. Repeating until the input list is empty
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy of the input list
    unsorted = arr.copy()
    result = []
    
    while unsorted:
        # Extract the first sublist
        sublist = [unsorted.pop(0)]
        
        # Iterate through remaining unsorted elements
        i = 0
        while i < len(unsorted):
            # If current element is greater than the last element in sublist, 
            # add it to sublist and remove from unsorted
            if unsorted[i] > sublist[-1]:
                sublist.append(unsorted.pop(i))
            else:
                i += 1
        
        # Merge the extracted sublist with the result list
        result = merge(result, sublist)
    
    return result

def merge(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    
    Returns:
        list: A merged sorted list
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
    
    # Append remaining elements from list1, if any
    merged.extend(list1[i:])
    
    # Append remaining elements from list2, if any
    merged.extend(list2[j:])
    
    return merged