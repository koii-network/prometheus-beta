def remove_unique_elements(my_list):
    """
    Remove unique (non-duplicate) elements from a list of integers 
    using only built-in list methods.
    
    Args:
        my_list (list): A list of integers
    
    Returns:
        list: A list containing only elements that appear more than once
    """
    # Create a new list to store elements that appear multiple times
    duplicates = []
    
    # Iterate through the list
    for num in my_list:
        # Check if the current number appears more than once in the original list
        if my_list.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    
    return duplicates