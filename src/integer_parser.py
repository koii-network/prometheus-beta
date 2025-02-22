def parse_and_sort_integers(input_string: str) -> list[int]:
    """
    Parse a comma-separated string of integers and return a sorted list.
    
    Args:
        input_string (str): A string containing integers separated by commas.
    
    Returns:
        list[int]: A sorted list of integers found in the input string.
    
    Examples:
        >>> parse_and_sort_integers("1,2,3")
        [1, 2, 3]
        >>> parse_and_sort_integers("3,1,2")
        [1, 2, 3]
        >>> parse_and_sort_integers("a1b,c2d,3e")
        [1, 2, 3]
        >>> parse_and_sort_integers("10,5,abc,15")
        [5, 10, 15]
    """
    # Extract only numeric characters, split by comma
    extracted_integers = []
    for item in input_string.split(','):
        # Use a list comprehension with integer parsing to remove non-numeric characters
        nums = [int(char) for char in item if char.isdigit()]
        if nums:
            # Convert a list of digits back to an integer
            extracted_integers.append(int(''.join(map(str, nums))))
    
    return sorted(extracted_integers)