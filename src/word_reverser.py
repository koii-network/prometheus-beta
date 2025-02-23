def reverse_words(input_string):
    """
    Reverse the order of words in a given string.

    Args:
        input_string (str): The input string to reverse.

    Returns:
        str: A string with words in reverse order, preserving spacing.

    Notes:
        - Handles multiple spaces between words
        - Ignores non-alphabetic characters
        - Preserves original spacing between words
    """
    # Handle empty or None input
    if not input_string:
        return ""

    # Split the string into words, handling multiple spaces
    words = input_string.split()

    # Reverse the words
    reversed_words = words[::-1]

    # Join the words back together, maintaining original spacing
    return " ".join(reversed_words)