def find_two_sum_indices(nums, target):
    """
    Find two indices in an array that add up to a target sum.
    
    Args:
        nums (list): A list of integers
        target (int): The target sum to find
    
    Returns:
        list: A list containing two indices where the corresponding 
              values add up to the target sum. Returns an empty list 
              if no such indices are found.
    
    Raises:
        TypeError: If inputs are not the correct type
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a number")
    
    # Create a dictionary to store complement values and their indices
    complement_dict = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices in order of first occurrence
            return [complement_dict[complement], i]
        
        # Store the current number and its index
        complement_dict[num] = i
    
    # Return an empty list if no solution is found
    return []