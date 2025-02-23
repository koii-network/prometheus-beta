def remove_unique_elements(my_list):
    """
    Remove unique elements from a list of integers, keeping only duplicates.
    
    Args:
        my_list (list): A list of integers
    
    Returns:
        list: A list containing only the elements that appear more than once
    """
    # Create a list to store duplicates
    duplicates = []
    
    # Iterate through the list
    for item in my_list:
        # If the item appears more than once and is not already in duplicates
        if my_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    
    return duplicates