def find_two_sum_indices(nums, target):
    """
    Find two indices in the array that add up to the target sum.
    
    Args:
        nums (list): A list of integers
        target (int): The target sum to find
    
    Returns:
        list: A list of two indices where the corresponding values add up to the target.
              Returns an empty list if no such indices are found.
    """
    # Create a dictionary to store complement values and their indices
    complement_dict = {}
    
    # Iterate through the array with index
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            return [complement_dict[complement], i]
        
        # Store the current number and its index
        complement_dict[num] = i
    
    # If no solution is found, return an empty list
    return []