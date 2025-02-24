def calculate_mixed_avg(numbers):
    """
    Calculate the average of the three smallest and three largest numbers in an array.
    
    Args:
        numbers (list): A list of six real numbers.
    
    Returns:
        float: The average of the three smallest and three largest numbers.
    
    Raises:
        ValueError: If the input list does not contain exactly 6 numbers.
    """
    # Validate input
    if len(numbers) != 6:
        raise ValueError("Input must be a list of exactly 6 numbers")
    
    # Sort the numbers 
    sorted_numbers = sorted(numbers)
    
    # Take three smallest and three largest numbers
    smallest_three = sorted_numbers[:3]
    largest_three = sorted_numbers[3:]
    
    # Calculate and return the average
    return (sum(smallest_three) + sum(largest_three)) / 6