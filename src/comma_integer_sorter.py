def sort_comma_integers(input_string: str) -> list:
    """
    Takes a string of integers separated by commas and returns a sorted list of integers.
    
    Args:
        input_string (str): A string containing comma-separated integers
    
    Returns:
        list: A sorted list of integers extracted from the input string
    
    Examples:
        >>> sort_comma_integers("3,1,4,1,5,9")
        [1, 1, 3, 4, 5, 9]
        >>> sort_comma_integers("10,abc,20,def,30")
        [10, 20, 30]
        >>> sort_comma_integers("")
        []
    """
    # Extract only integer values, ignoring non-integer characters
    integers = []
    for item in input_string.split(','):
        try:
            # Remove any non-digit characters and convert to integer
            cleaned_item = ''.join(char for char in item if char.isdigit())
            if cleaned_item:
                integers.append(int(cleaned_item))
        except ValueError:
            # Skip items that cannot be converted to integers
            continue
    
    # Return the sorted list of integers
    return sorted(integers)