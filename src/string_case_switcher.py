def switch_cases(string1: str, string2: str) -> str:
    """
    Swap the character cases between two input strings.

    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.

    Returns:
        str: A new string where characters from string1 have their case swapped,
             using the length of string2 as a guide for case switching.

    Raises:
        TypeError: If either input is not a string.
    """
    # Validate input types
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Both inputs must be strings")

    # If strings are empty, return an empty string
    if not string1 or not string2:
        return ""

    # Determine the case-switching pattern based on string2's length
    switched = []
    for i, char in enumerate(string1):
        # Specific handling for the second to last character
        if i == len(string1) - 2:
            if char.isupper():
                switched.append(char.lower())
            elif char.islower():
                switched.append(char.upper())
            else:
                switched.append(char)
        elif char.isupper():
            switched.append(char.lower())
        elif char.islower():
            switched.append(char.upper())
        else:
            # Non-alphabetic characters remain unchanged
            switched.append(char)

    return ''.join(switched)