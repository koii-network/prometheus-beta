def calculate_number_range(number_string):
    """
    Calculate and print the difference between the largest and smallest numbers 
    in a comma-separated string of integers.
    
    Args:
        number_string (str): A string of comma-separated integers
    
    Raises:
        ValueError: If the input string is empty or contains non-integer values
    """
    # Remove whitespace and split the string
    try:
        numbers = [int(num.strip()) for num in number_string.split(',')]
        
        # Check if the list is empty
        if not numbers:
            raise ValueError("Input string is empty")
        
        # Find the difference between max and min
        range_difference = max(numbers) - min(numbers)
        
        # Print the result
        print(range_difference)
        
        return range_difference
    except ValueError as e:
        # Handle conversion errors or empty input
        raise ValueError(f"Invalid input: {str(e)}")