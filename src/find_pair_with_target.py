def find_pair_with_target(nums, target):
    """
    Find index pairs in a list of unique integers where the numbers at those 
    indices add up to the target sum.
    
    Args:
    nums (list): A list of unique integers
    target (int): The target sum to find
    
    Returns:
    list: A list of index pairs where nums[i] + nums[j] == target
    """
    # Create a dictionary to store complement values and their indices
    complement_dict = {}
    
    # Store index pairs to return
    result = []
    
    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Add the index pairs to the result
            result.append([complement_dict[complement], i])
        
        # Store the current number's index for future lookups
        complement_dict[num] = i
    
    return result