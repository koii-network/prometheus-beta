def remove_unique_elements(my_list):
    """
    Remove duplicate values from a list of integers using only built-in list methods.
    
    Args:
        my_list (list): A list of integers
    
    Returns:
        list: A new list containing only elements that appear more than once
    """
    # Create a list to store duplicates
    duplicates = []
    
    # Iterate through the list and check for duplicates
    for num in my_list:
        # Check if the current number appears more than once in the original list
        if my_list.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    
    return duplicates