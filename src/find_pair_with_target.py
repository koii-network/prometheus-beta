def find_pair_with_target(nums, target):
    """
    Find index pairs of unique integers that sum up to the target.
    
    Args:
        nums (list): A list of unique integers
        target (int): The target sum to find
    
    Returns:
        list: A list of index pairs where nums[i] + nums[j] == target
    """
    # Create a dictionary to store complement values and their indices
    complement_dict = {}
    
    # List to store the result index pairs
    result = []
    
    # Iterate through the list with index
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Add the index pair to the result
            result.append([complement_dict[complement], i])
        
        # Store the current number's index 
        complement_dict[num] = i
    
    return result