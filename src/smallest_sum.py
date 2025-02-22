def find_smallest_sum(list1, list2):
    """
    Find the smallest possible sum by pairing elements from two lists.
    
    Args:
        list1 (list): First list of integers
        list2 (list): Second list of integers
    
    Returns:
        int: The smallest possible sum that can be created by pairing 
             elements from the two lists
    
    Raises:
        ValueError: If either input is not a list or lists have different lengths
    """
    # Input validation
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    
    if len(list1) != len(list2):
        raise ValueError("Input lists must have the same length")
    
    # Sort both lists 
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2, reverse=True)
    
    # Calculate the smallest possible sum
    return sum(a * b for a, b in zip(sorted_list1, sorted_list2))