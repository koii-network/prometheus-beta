def calculate_six_number_average(numbers):
    """
    Calculate the average of the three smallest and three largest numbers in a list of six real numbers.
    
    Args:
        numbers (list): A list of six real numbers
    
    Returns:
        float: The average of the three smallest and three largest numbers
    
    Raises:
        ValueError: If the input list does not contain exactly six numbers
    """
    # Validate input
    if len(numbers) != 6:
        raise ValueError("Input must be a list of exactly six numbers")
    
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    
    # Take the first three (smallest) and last three (largest) numbers
    smallest_three = sorted_numbers[:3]
    largest_three = sorted_numbers[3:]
    
    # Calculate the average of the smallest and largest three numbers
    average = (sum(smallest_three) + sum(largest_three)) / 6
    
    return average