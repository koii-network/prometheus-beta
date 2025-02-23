def parse_and_sort_csv_integers(input_string: str) -> list[int]:
    """
    Parse a comma-separated string of integers and return a sorted list.

    This function:
    - Extracts only integer values from the input string
    - Discards any non-integer characters
    - Returns the extracted integers in sorted order
    - Handles empty strings and strings with no valid integers
    
    Args:
        input_string (str): A string containing comma-separated integers
    
    Returns:
        list[int]: A sorted list of extracted integers
    
    Examples:
        >>> parse_and_sort_csv_integers("3,1,4,1,5,9")
        [1, 1, 3, 4, 5, 9]
        >>> parse_and_sort_csv_integers("10,abc,20,def,30")
        [10, 20, 30]
        >>> parse_and_sort_csv_integers("")
        []
    """
    # If input is empty or None, return an empty list
    if not input_string:
        return []
    
    # Split the string and attempt to convert each part to an integer
    parsed_integers = []
    for part in input_string.split(','):
        # Remove any whitespace and try to convert to integer
        try:
            # Filter out non-digit characters, keeping negative sign if present
            cleaned_part = ''.join(char for char in part.strip() if char.isdigit() or char == '-')
            
            # Convert to integer if not empty after cleaning
            if cleaned_part:
                parsed_integers.append(int(cleaned_part))
        except ValueError:
            # Skip any parts that can't be converted to an integer
            continue
    
    # Return the sorted list of parsed integers
    return sorted(parsed_integers)