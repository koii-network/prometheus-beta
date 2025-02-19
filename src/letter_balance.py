def check_letter_balance(input_string):
    """
    Check if a given string contains the same number of uppercase and lowercase letters.
    
    Args:
        input_string (str): The input string to check for letter balance.
    
    Returns:
        str: 'Balanced' if uppercase and lowercase letter counts are equal,
             'Not Balanced' otherwise.
    
    Rules:
    1. Spaces and punctuation marks are allowed
    2. Only count uppercase and lowercase letters
    3. Input must contain at least one letter
    4. Case-sensitive comparison
    """
    # Check if the input string is empty
    if not input_string:
        return 'Not Balanced'
    
    # Count uppercase and lowercase letters
    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())
    
    # Check if there's at least one letter
    if uppercase_count + lowercase_count == 0:
        return 'Not Balanced'
    
    # Compare counts and return result
    return 'Balanced' if uppercase_count == lowercase_count else 'Not Balanced'

def main():
    # Example usage
    test_strings = [
        "Hello World",  # Balanced
        "Python LANGUAGE",  # Not Balanced
        "AbCdEfG",  # Balanced
        "123!@#",  # Not Balanced
        ""  # Not Balanced
    ]
    
    for string in test_strings:
        print(f"'{string}': {check_letter_balance(string)}")

if __name__ == "__main__":
    main()