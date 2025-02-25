def sort_csv_integers(input_string: str) -> list[int]:
    """
    Parses a string of comma-separated integers and returns a sorted list.

    Args:
        input_string (str): A string containing integers separated by commas.
                             Non-integer characters are discarded.

    Returns:
        list[int]: A sorted list of integers extracted from the input string.

    Examples:
        >>> sort_csv_integers("5,2,8,1")
        [1, 2, 5, 8]
        >>> sort_csv_integers("10, 20abc, 30def")
        [10, 20, 30]
        >>> sort_csv_integers("")
        []
    """
    # Handle empty string case
    if not input_string:
        return []
    
    # Extract and convert integers, discarding non-numeric parts
    integers = []
    for item in input_string.split(','):
        # Remove whitespace and non-digit characters
        cleaned_item = ''.join(char for char in item.strip() if char.isdigit())
        
        # Convert to integer if not empty
        if cleaned_item:
            try:
                integers.append(int(cleaned_item))
            except ValueError:
                # Skip items that can't be converted to integers
                continue
    
    # Return sorted list of integers
    return sorted(integers)