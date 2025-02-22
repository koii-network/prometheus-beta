def convert_to_roman_numeral(number: int) -> str:
    """
    Convert a non-negative integer to its Roman numeral representation.
    
    Args:
        number (int): An integer between 0 and 3999 (inclusive)
    
    Returns:
        str: Roman numeral representation of the input number
    
    Raises:
        ValueError: If the input is not between 0 and 3999
    """
    # Input validation
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0 or number > 3999:
        raise ValueError("Input must be between 0 and 3999")
    
    # Special case for 0
    if number == 0:
        return ""
    
    # Define Roman numeral symbols and their corresponding values
    roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    # Build Roman numeral string
    result = []
    for value, symbol in roman_map:
        while number >= value:
            result.append(symbol)
            number -= value
    
    return ''.join(result)