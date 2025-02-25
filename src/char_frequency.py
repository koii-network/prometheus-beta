def count_character_frequency(input_string: str) -> dict:
    """
    Count the frequency of characters in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Use a dictionary comprehension to count character frequencies
    return {char: input_string.count(char) for char in set(input_string)}