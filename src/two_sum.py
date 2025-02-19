def two_sum(nums, target):
    """
    Find two indices in the array that add up to the target sum.
    
    Args:
        nums (list): A list of integers
        target (int): The target sum to find
    
    Returns:
        list: A list of two indices where the corresponding numbers add up to the target
               Returns an empty list if no such indices are found
    """
    # Create a dictionary to store complement values and their indices
    complement_dict = {}
    
    # Iterate through the list with enumeration to track indices
    for i, num in enumerate(nums):
        complement = target - num
        
        # If the complement exists in the dictionary, we found our pair
        if complement in complement_dict:
            return [complement_dict[complement], i]
        
        # Store the current number's index
        complement_dict[num] = i
    
    # If no solution is found, return an empty list
    return []