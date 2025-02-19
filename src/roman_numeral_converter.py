def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.
    
    Args:
        num (int): A non-negative integer between 0 and 3999.
    
    Returns:
        str: The Roman numeral representation of the input number.
    
    Raises:
        ValueError: If the input is not between 0 and 3999.
    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    if num < 0 or num > 3999:
        raise ValueError("Input must be between 0 and 3999")
    
    # Special case for 0
    if num == 0:
        return ""
    
    # Define Roman numeral symbols and their values
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
    
    # Build the Roman numeral representation
    result = ""
    for value, symbol in roman_map:
        while num >= value:
            result += symbol
            num -= value
    
    return result