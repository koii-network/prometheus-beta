def find_number_range_difference(number_string):
    """
    Takes a string of comma-separated integers and prints the difference 
    between the largest and smallest numbers in the string.
    
    Args:
        number_string (str): A string of comma-separated integers
    
    Raises:
        ValueError: If the input string is empty or contains non-integer values
    """
    # Remove any whitespace and split the string
    try:
        # Convert string to list of integers, removing any whitespace
        numbers = [int(num.strip()) for num in number_string.split(',')]
        
        # Check if the list is empty
        if not numbers:
            raise ValueError("Input string is empty")
        
        # Find the difference between max and min
        difference = max(numbers) - min(numbers)
        
        # Print the difference
        print(difference)
        
        # Also return the difference for testing purposes
        return difference
    except ValueError as e:
        # Catch conversion errors or empty input
        raise ValueError(f"Invalid input: {str(e)}")