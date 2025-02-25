def check_letter_case_balance(input_string):
    """
    Check if a given string contains an equal number of uppercase and lowercase letters.
    
    Args:
        input_string (str): The input string to check for letter case balance.
    
    Returns:
        str: 'Balanced' if uppercase and lowercase letter counts are equal, 
             'Not Balanced' otherwise.
    
    Raises:
        ValueError: If the input string contains no letters.
    """
    # Filter uppercase and lowercase letters
    uppercase_letters = [char for char in input_string if char.isupper()]
    lowercase_letters = [char for char in input_string if char.islower()]
    
    # Check if there are any letters in the string
    if not uppercase_letters and not lowercase_letters:
        raise ValueError("Input string must contain at least one letter")
    
    # Compare the counts of uppercase and lowercase letters
    if len(uppercase_letters) == len(lowercase_letters):
        return 'Balanced'
    else:
        return 'Not Balanced'