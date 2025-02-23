def parse_and_sort_integers(input_string):
    """
    Parse a comma-separated string of integers and return a sorted list.
    
    Args:
        input_string (str): A string containing integers separated by commas.
    
    Returns:
        list: A sorted list of integers extracted from the input string.
    """
    # Remove any non-digit and non-comma characters
    cleaned_string = ''.join(char for char in input_string if char.isdigit() or char == ',')
    
    # Split the string and convert to integers, filtering out empty strings
    try:
        integers = [int(num.strip()) for num in cleaned_string.split(',') if num.strip()]
    except ValueError:
        # Return an empty list if any conversion fails
        return []
    
    # Sort and return the list of integers
    return sorted(integers)