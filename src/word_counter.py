def count_words(text: str) -> int:
    """
    Count the number of words in a given string.

    A word is defined as a sequence of non-whitespace characters.
    Handles multiple whitespace characters, leading/trailing whitespace.

    Args:
        text (str): The input string to count words in.

    Returns:
        int: The number of words in the string.

    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Handle empty or whitespace-only strings
    if not text.strip():
        return 0

    # Split by whitespace and count non-empty elements
    return len(text.split())