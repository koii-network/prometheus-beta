def calculate_small_large_average(numbers):
    """
    Calculate the average of the three smallest and three largest numbers in a list of six real numbers.
    
    Args:
        numbers (list): A list of six real numbers.
    
    Returns:
        float: The average of the three smallest and three largest numbers.
    
    Raises:
        ValueError: If the input list does not contain exactly six numbers.
    """
    # Validate input
    if len(numbers) != 6:
        raise ValueError("Input must contain exactly six numbers")
    
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    
    # Calculate average of three smallest and three largest numbers
    small_average = sum(sorted_numbers[:3]) / 3
    large_average = sum(sorted_numbers[3:]) / 3
    
    return (small_average + large_average) / 2