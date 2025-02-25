"""
Module for converting strings to path case.

Path case is a string formatting style where:
- All characters are lowercase
- Spaces, underscores, and camel case are converted to hyphens
- Consecutive separators are reduced to a single hyphen
- Leading/trailing separators are removed
"""

import re


def to_path_case(input_string: str) -> str:
    """
    Convert a given string to path case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string converted to path case.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> to_path_case("Hello World")
        'hello-world'
        >>> to_path_case("snake_case_string")
        'snake-case-string'
        >>> to_path_case("camelCaseString")
        'camel-case-string'
        >>> to_path_case("  Mixed  Separators  ")
        'mixed-separators'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Handle empty string
    if not input_string.strip():
        return ""

    # Convert camel case to lowercase with hyphens
    # This step converts camelCase to camel-case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1)

    # Replace multiple separators with a single hyphen and convert to lowercase
    s3 = re.sub(r'[_\s]+', '-', s2.lower())
    
    # Remove leading and trailing hyphens and replace multiple consecutive hyphens
    s4 = re.sub(r'-+', '-', s3).strip('-')

    return s4