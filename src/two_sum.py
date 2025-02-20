def find_two_sum(numbers, target):
    """
    Find two numbers in the given array that add up to the target number.
    
    Args:
        numbers (list): A list of integers to search through
        target (int): The target sum to find
    
    Returns:
        list: A list containing the indices of the two numbers that add up to the target
              Returns an empty list if no such pair is found
    """
    # Create a dictionary to store complement values and their indices
    num_dict = {}
    
    # Iterate through the array with enumerate to keep track of indices
    for index, num in enumerate(numbers):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # Return the indices of the two numbers
            return [num_dict[complement], index]
        
        # Store the current number and its index
        num_dict[num] = index
    
    # Return an empty list if no solution is found
    return []