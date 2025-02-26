def parse_and_sort_integers(input_string: str) -> list[int]:
    """
    Parse a comma-separated string of integers and return a sorted list.
    
    Discards any non-integer characters from the input string.
    
    Args:
        input_string (str): A string containing integers separated by commas
    
    Returns:
        list[int]: A sorted list of integers extracted from the input string
    
    Examples:
        >>> parse_and_sort_integers("1,2,3")
        [1, 2, 3]
        >>> parse_and_sort_integers("10,5,abc2,3def")
        [2, 3, 5, 10]
        >>> parse_and_sort_integers("")
        []
    """
    # Extract only integer characters and convert to integers
    integers = []
    # Split the string and process each potential number
    for item in input_string.split(','):
        # Remove any non-digit characters
        cleaned_item = ''.join(char for char in item if char.isdigit())
        
        # Convert to integer if not empty
        if cleaned_item:
            try:
                integers.append(int(cleaned_item))
            except ValueError:
                # Skip if conversion fails (though this should be rare with above cleaning)
                continue
    
    # Return sorted list of integers
    return sorted(integers)