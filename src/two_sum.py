def two_sum(nums, target):
    """
    Find two numbers in the array that add up to the target number.
    
    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find
    
    Returns:
        list: A list of two indices where the numbers add up to the target.
              Returns an empty list if no such pair is found.
    """
    # Create a dictionary to store complements
    complement_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Store the current number and its index
        complement_dict[num] = i
    
    # If no solution is found
    return []