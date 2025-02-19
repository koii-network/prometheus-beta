def find_two_sum_indices(nums, target):
    """
    Find two indices in the array that add up to the target sum.
    
    Args:
        nums (list): A list of integers
        target (int): The target sum to find
    
    Returns:
        list: A list of two indices where the values add up to the target,
              or an empty list if no such indices exist
    """
    # Create a dictionary to store complements
    complement_dict = {}
    
    # Iterate through the array with enumeration to keep track of indices
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Store the current number's index
        complement_dict[num] = i
    
    # If no solution is found, return an empty list
    return []