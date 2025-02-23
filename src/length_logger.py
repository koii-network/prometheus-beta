import logging
from typing import Union, Sequence

def log_length(input_value: Union[str, Sequence]) -> int:
    """
    Log the length of a given string or array/sequence.

    Args:
        input_value (str or Sequence): The input to measure length of.

    Returns:
        int: The length of the input.

    Raises:
        TypeError: If the input is not a string or a sequence.
    """
    # Validate input type
    if not isinstance(input_value, (str, Sequence)):
        raise TypeError("Input must be a string or a sequence (list, tuple, etc.)")
    
    # Calculate length
    length = len(input_value)
    
    # Log the length
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(f"Length: {length}")
    
    return length